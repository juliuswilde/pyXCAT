from pydantic import BaseModel, Field


class ImageParameters(BaseModel):
    """What the program runs (mode + motion), what it writes out, and the sampling
    grid the phantom is rasterised onto."""

    ### Program mode ###
    mode: int = Field(default=0, ge=0, le=5, alias="mode", description="program mode (0 = phantom, 1 = lesion (heart or kidneys), 2 = spherical lesion, 3 = plaque, 4 = vectors, 5 = save anatomical variation) SEE NOTE 0")
    motion_option: int = Field(default=0, ge=0, le=2, alias="motion_option", description="motion_option (0=beating heart only, 1=respiratory motion only, 2=both motions) see NOTE 2")

    ### Voxelised output ###
    atten_phan_each: bool = Field(default=False, alias="atten_phan_each", description="attenuation_coeff_phantom_each_frame (1=save phantom to file, 0=don't save)")
    act_phan_each: bool = Field(default=True, alias="act_phan_each", description="activity_phantom_each_frame (1=save phantom to file, 0=don't save)")

    atten_phan_ave: bool = Field(default=False, alias="atten_phan_ave", description="attenuation_coeff_phantom_average  (1=save, 0=don't save) see NOTE 1")
    act_phan_ave: bool = Field(default=False, alias="act_phan_ave", description="activity_phantom_average  (1=save, 0=don't save) see NOTE 1")

    activ_output_format: int = Field(default=0, ge=0, le=2, alias="activ_output_format", description="output format for act_phan_each phantom (0 = 32 bit float, 1 = 16 bit integer, 2 = 8 bit)")
    color_code: bool = Field(default=True, alias="color_code", description="color_code (1 = save the phantom as an activity phantom with each structure set to unique integer value, 0 = do not save)")
    output_material_id: bool = Field(default=False, alias="output_material_id", description="write the organ intensity/material IDs to organ_ids.txt (0 = do not write, 1 = write)")

    # slice_output requires subvoxel_index = 1 and is rejected in mode 4 (vectors).
    slice_output: bool = Field(default=False, alias="slice_output", description="write the phantom slice by slice (0 = no, 1 = yes); requires subvoxel_index = 1 and cannot be used with mode = 4")
    ct_output: bool = Field(default=False, alias="ct_output", description="write the attenuation phantom in CT output format (0 = no, 1 = yes)")

    ### NURBS / mesh output ###
    nurbs_save: bool = Field(default=False, alias="nurbs_save", description="nurbs_save (1 = save the phantom in NURBS format, 0 = do not save)")
    nurbs_frame_save: bool = Field(default=False, alias="nurbs_frame_save", description="save the NURBS surfaces of every time frame to <out_base>_frame_<n>.nrb (0 = no, 1 = yes)")
    mesh_save: bool = Field(default=False, alias="mesh_save", description="mesh_save (1 = save the phantom as meshes, 0 = do not save)")
    output_intestines: bool = Field(default=False, alias="output_intestines", description="save the intestine NURBS surfaces per frame to <out_base>_intestines_frame_<n>.nrb (0 = no, 1 = yes)")

    ### Timing ###
    out_period: float = Field(default=0.0, ge=0.0, alias="out_period", description="output_period (SECS) (if <= 0, then output_period=time_per_frame*output_frames)")
    time_per_frame: float = Field(default=1.0, ge=0, alias="time_per_frame", description="time_per_frame (SECS) (**IGNORED unless out_period<=0**)")
    out_frames: int = Field(default=1, ge=1, alias="out_frames", description="output_frames (# of output time frames )")

    ### Sampling grid ###
    pixel_width: float = Field(default=0.625, gt=0, alias="pixel_width", description="pixel width (cm); see NOTE 7")
    slice_width: float = Field(default=0.625, gt=0, alias="slice_width", description="slice width (cm);")
    x_array_size: int = Field(default=128, alias="x_array_size", gt=1, description="x array size")
    y_array_size: int = Field(default=128, gt=1, alias="y_array_size", description="y array size")
    subvoxel_index: int = Field(default=1, ge=1, le=4, alias="subvoxel_index", description="subvoxel_index (=1,2,3,4 -> 1,8,27,64 subvoxels/voxel, respectively)")
    startslice: int = Field(default=100, ge=1, alias="startslice", description="start slice")
    endslice: int = Field(default=227, ge=1, alias="endslice", description="end slice")
    use_res: int = Field(default=0, ge=0, le=1, alias="use_res", description="0 = use high resolution to calc volumes, 1 = use pixel_width and slice_width")

    ### Vector output (mode = 4); see NOTE 12 ###
    vec_factor: int = Field(default=1, ge=1, alias="vec_factor", description="higher number will increase the precision of the vector output")
    mode4_include_tumor: bool = Field(default=False, alias="mode4_include_tumor", description="include the lesion/tumor surface in the mode 4 vector output (0 = no, 1 = yes)")

    ### Misc ###
    kidney_name_flag: bool = Field(default=False, alias="kidney_name_flag", description="use the separate cortex/medulla/renal pelvis names for the kidney structures (0 = no, 1 = yes)")
