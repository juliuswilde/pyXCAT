from pathlib import Path

from pydantic import BaseModel, Field

class LesionParameters(BaseModel):

    tumor_filename: Path = Field(default=Path("lesion.nrb"), alias="tumor_filename", description="Name of lesion file, the default file lesion.nrb defines a sphere with diameter = 1.0 mms")

    tumor_motion_filename: Path = Field(default=Path("tumor_trans_curve.dat"), alias="tumor_motion_filename", description="Name of user defined translational motion curve for tumor")
    tumor_rotation_filename: Path = Field(default=Path("tumor_rot_curve.dat"), alias="tumor_rotation_filename", description="Name of user defined rotational motion curve for tumor")
    