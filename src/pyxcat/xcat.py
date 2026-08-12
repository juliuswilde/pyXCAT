from pathlib import Path
import time
import subprocess
import logging

from pyxcat.parameters import XCATParameters

class XCAT:

    def __init__(self, path_to_xcat_exe: Path):

        self.xcat_path = path_to_xcat_exe

        self.logger = logging.getLogger(__name__)


    def generate(self, params: XCATParameters, save_dir: Path, run_name: str = "XCAT_Phantom", post_processing_options: dict = None):

        if not save_dir.exists() or not save_dir.is_dir():
            save_dir.mkdir(parents=True)

        parameter_path = save_dir / f"{run_name}_used_parameters.par"
        params.save_as_par(parameter_path)

        command = f"{self.xcat_path} {parameter_path} {save_dir / run_name}"

        self.logger.info("Starting to phantom generation" + "\n" + "*"*20)
        start_time = time.time()

        process = subprocess.Popen(command)#, stdout=subprocess.PIPE)
        out, err = process.communicate()

        stop_time = time.time()
        self.logger.info("\n" + "*"*20 + f"Phantom generated in {(stop_time - start_time):.1f}s\n" + "*"*20)

        #if not post_processing_options:
        #    return

        if True:#post_processing_options.get("to_nifti"):
            self._convert_output_to_nifti(params, save_dir, run_name)


    def _convert_output_to_nifti(self, params: XCATParameters, save_dir: Path, run_name: str) -> list[Path]:
        """Stitch the raw .bin output into NIfTI files, one per enabled output.

        Produces up to four files: a 4D volume per frame-wise output
        (_act / _atn) and a 3D volume per averaged output (_act_av / _atn_av).
        """
        import numpy as np
        import nibabel as nib

        image_params = params.image_params

        # XCAT writes the volume slice by slice, each slice a y-by-x plane, so
        # the file is ordered with x varying fastest.
        n_slices = image_params.endslice - image_params.startslice + 1
        file_shape = (n_slices, image_params.y_array_size, image_params.x_array_size)

        # The .par widths are in cm, NIfTI works in mm.
        in_plane = image_params.pixel_width * 10
        through_plane = image_params.slice_width * 10

        if image_params.out_period > 0:
            frame_time = image_params.out_period / image_params.out_frames
        else:
            frame_time = image_params.time_per_frame

        affine = np.diag([in_plane, in_plane, through_plane, 1.0])
        # Keep runs with different slice ranges in a common frame of reference.
        affine[2, 3] = (image_params.startslice - 1) * through_plane

        frame_stems = [f"{i}" for i in range(1, image_params.out_frames + 1)]
        outputs = []
        for tag, each, average in (
            ("act", image_params.act_phan_each, image_params.act_phan_ave),
            ("atn", image_params.atten_phan_each, image_params.atten_phan_ave),
        ):
            if each:
                outputs.append((tag, frame_stems, True))
            if average:
                outputs.append((f"{tag}_av", ["av"], False))

        written = []
        for name, stems, dynamic in outputs:
            tag = name.removesuffix("_av")
            sources = [save_dir / f"{run_name}_{tag}_{stem}.bin" for stem in stems]

            missing = [p for p in sources if not p.exists()]
            if missing:
                self.logger.warning(
                    f"Skipping {name} NIfTI, missing output: {', '.join(p.name for p in missing)}"
                )
                continue

            # Fill a preallocated array rather than stacking, so the frames are
            # only held in memory once.
            data = np.empty(
                (image_params.x_array_size, image_params.y_array_size, n_slices, len(sources)),
                dtype=np.float32,
            )
            for index, source in enumerate(sources):
                data[..., index] = self._read_raw_volume(source, file_shape)

            if not dynamic:
                data = data[..., 0]

            image = nib.Nifti1Image(data, affine)
            image.header.set_xyzt_units("mm", "sec")
            if dynamic:
                image.header.set_zooms((in_plane, in_plane, through_plane, frame_time))

            destination = save_dir / f"{run_name}_{name}.nii.gz"
            nib.save(image, destination)
            written.append(destination)
            self.logger.info(f"Wrote {destination.name} {data.shape}")

        return written


    @staticmethod
    def _read_raw_volume(path: Path, file_shape: tuple[int, int, int]):
        """Read one raw XCAT volume and reorder it from (slice, y, x) to (x, y, slice)."""
        import numpy as np

        raw = np.fromfile(path, dtype="<f4")

        expected = file_shape[0] * file_shape[1] * file_shape[2]
        if raw.size != expected:
            raise ValueError(
                f"{path.name} holds {raw.size} voxels, but the parameters describe "
                f"{expected} ({file_shape[2]}x{file_shape[1]}x{file_shape[0]})"
            )

        return raw.reshape(file_shape).transpose(2, 1, 0)

