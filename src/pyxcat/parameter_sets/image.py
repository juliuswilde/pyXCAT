from pydantic import BaseModel, Field

class ImageParameters(BaseModel):
    mode: int = Field(default=0, ge=0, le=5, alias="mode", description="# program mode (0 = phantom, 1 = lesion (heart or kidneys), 2 = spherical lesion, 3 = plaque, 4 = vectors, 5 = save anatomical variation) SEE NOTE 0")

    atten_phan_each: bool = Field(default=False, alias="atten_phan_each", description="attenuation_coeff_phantom_each_frame (1=save phantom to file, 0=don't save)")
    act_phan_each: bool = Field(default=True, alias="act_phan_each", description="activity_phantom_each_frame (1=save phantom to file, 0=don't save)")

    atten_phan_ave: bool = Field(default=False, alias="atten_phan_ave", description="attenuation_coeff_phantom_average  (1=save, 0=don't save) see NOTE 1")
    act_phan_ave: bool = Field(default=False, alias="act_phan_ave", description="activity_phantom_average  (1=save, 0=don't save) see NOTE 1")

    color_code: bool = Field(default=True, alias="color_code", description="color_code (1 = save the phantom as an activity phantom with each structure set to unique integer value, 0 = do not save)")

    out_period: float = Field(default=0.0, ge=0.0, alias="out_period", description="output_period (SECS) (if <= 0, then output_period=time_per_frame*output_frames)")
    time_per_frame: float = Field(default=1.0, ge=0, alias="time_per_frame", description="time_per_frame (SECS) (**IGNORED unless out_period<=0**)")
    out_frames: int = Field(default=2, ge=1, alias="out_frames", description="output_frames (# of output time frames )")

    pixel_width: float = Field(default=0.625, gt=0, alias="pixel_width", description="pixel width (cm); see NOTE 7")
    slice_width: float = Field(default=0.625, gt=0, alias="slice_width", description="slice width (cm);")
    x_array_size: int = Field(default=128, alias="x_array_size", gt=1, description="x array size")
    y_array_size: int = Field(default=128, gt=1, alias="y_array_size", description="y array size")
    subvoxel_index: int = Field(default=1, ge=1, le=4, alias="subvoxel_index", description="subvoxel_index (=1,2,3,4 -> 1,8,27,64 subvoxels/voxel, respectively)")
    startslice: int = Field(default=100, ge=1, alias="startslice", description="start slice")
    endslice: int = Field(default=227, ge=1, alias="endslice", description="end slice")
    use_res: int = Field(default=0, ge=0, le=1, alias="use_res", description="0 = use high resolution to calc volumes, 1 = use pixel_width and slice_width")
