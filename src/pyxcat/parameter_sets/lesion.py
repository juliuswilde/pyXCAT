from pathlib import Path
from typing import Literal

from pydantic import BaseModel, Field


class LesionParameters(BaseModel):
    """Lesion, tumour and plaque models.

    Only used by modes 1-3 (and by ``motion_defect_flag`` in mode 0). The executable
    defaults every geometric extent here to 0, which produces a degenerate zero-sized
    lesion; the sample parameter file values are used instead where that is the case.
    """

    ### Heart / kidney lesion; see NOTE 9 ###
    motion_defect_flag: bool = Field(default=False, alias="motion_defect_flag", description="(0 = do not include, 1 = include) regional motion abnormality in the LV as defined by heart lesion parameters see NOTE 9")

    lesion_type: int = Field(default=0, ge=0, le=2, alias="lesion_type", description="type of lesion to model (0 = heart, 1 = right kidney, 2 = left kidney)")

    ThetaCenter: float = Field(default=0.0, ge=0.0, le=360.0, alias="ThetaCenter", description="theta center in deg. (between 0 and 360)")
    ThetaWidth: float = Field(default=100.0, ge=0.0, le=360.0, alias="ThetaWidth", description="theta width in deg., total width (between 0 and 360 deg.)")
    XCenterIndex: float = Field(default=0.5, ge=0.0, le=1.0, alias="XCenterIndex", description="x center (For heart 0.0=base, 1.0=apex, For kidneys 0.0 = top, 1.0 = bottom, other fractions=distances in between)")
    XWidthIndex: float = Field(default=60.0, ge=0.0, alias="XWidthIndex", description="x width, total in mm's")
    Wall_fract: float = Field(default=1.0, ge=0.0, le=1.0, alias="Wall_fract", description="wall_fract, fraction of the outer wall transgressed by the lesion")

    ### Heart lesion motion ###
    motion_scale: float = Field(default=1.0, ge=0.0, alias="motion_scale", description="scales the motion of the defect region in the heart (1 = normal motion, < 1 = reduced motion), altered motion blends with normal")
    border_zone_long: int = Field(default=1, ge=1, alias="border_zone_long", description="longitudinal width (in terms of number of control points) of transition between abnormal and normal motion of heart lesion")
    border_zone_radial: int = Field(default=1, ge=1, alias="border_zone_radial", description="radial width (in terms of number of control points) of transition between abnormal and normal motion of heart lesion")

    ### Spherical lesion; see NOTE 10 ###
    tumor_filename: Path = Field(default=Path("lesion.nrb"), alias="tumor_filename", description="Name of lesion file, the default file lesion.nrb defines a sphere with diameter = 1.0 mms")
    x_location: float = Field(default=102.0, ge=0.0, alias="x_location", description="x coordinate (pixels) to place lesion")
    y_location: float = Field(default=124.0, ge=0.0, alias="y_location", description="y coordinate (pixels) to place lesion")
    z_location: float = Field(default=26.0, ge=0.0, alias="z_location", description="z coordinate (pixels) to place lesion")
    lesn_diameter: float = Field(default=10.0, gt=0.0, alias="lesn_diameter", description="Diameter of lesion (mm), scaling factor for models other than lesion.nrb")
    tumor_location_flag: int = Field(default=0, ge=0, le=1, alias="tumor_location_flag", description="Tumor location (0 = in organ, 1 = in body/breast)")

    tumor_motion_flag: int = Field(default=0, ge=0, le=1, alias="tumor_motion_flag", description="Sets tumor motion (0 = default motion based on lungs, 1 = motion defined by user curve below)")
    tumor_motion_filename: Path = Field(default=Path("tumor_trans_curve.dat"), alias="tumor_motion_filename", description="Name of user defined translational motion curve for tumor")
    tumor_rotation_flag: int = Field(default=0, ge=0, le=1, alias="tumor_rotation_flag", description="Include rotational motion for the tumor (0 = no, 1 = yes)")
    tumor_rotation_filename: Path = Field(default=Path("tumor_rot_curve.dat"), alias="tumor_rotation_filename", description="Name of user defined rotational motion curve for tumor")

    ### Coronary plaque; see NOTE 11 ###
    p_center_v: float = Field(default=0.2, ge=0.0, le=1.0, alias="p_center_v", description="plaque center along the length of the artery (between 0 and 1)")
    p_center_u: float = Field(default=0.5, ge=0.0, le=1.0, alias="p_center_u", description="plaque center along the circumference of the artery (between 0 and 1)")
    p_height: float = Field(default=1.0, gt=0.0, alias="p_height", description="plaque thickness in mm.")
    p_width: float = Field(default=2.0, gt=0.0, alias="p_width", description="plaque width in mm.")
    p_length: float = Field(default=5.0, gt=0.0, alias="p_length", description="plaque length in mm.")
    p_id: Literal["aorta", "rca1", "rca2", "lad1", "lad2", "lad3", "lcx"] = Field(default="aorta", alias="p_id", description="vessel ID to place the plaque in")
