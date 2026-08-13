from pathlib import Path

from pydantic import BaseModel, Field

class BodyParameters(BaseModel):
    gender: int = Field(default=0, ge=0, le=1, alias="gender", description="male or female phantom (0 = male, 1 = female), be sure to adjust below accordingly")

    organ_file: Path = Field(default=Path("vmale50.nrb"), alias="organ_file", description="name of organ file that defines all organs (male = vmale50.nrb, female - vfemale50.nrb)")
    heart_base: Path = Field(default=Path("vmale50_heart.nrb"), alias="heart_base", description="basename for heart files (male = vmale50_heart.nrb; female = vfemale50_heart.nrb)")

    breast_type: int = Field(default=1, ge=0, le=1, alias="breast_type", description="breast_type (0=supine, 1=prone)")
    which_breast: int = Field(default=0, ge=0, le=3, alias="which_breast", description="which_breast (0 = none, 1 = both, 2 = right only, 3=left only )")

    arms_flag: int = Field(default=0, ge=0, le=1, alias="arms_flag", description="arms_flag (0 = no arms, 1 = arms at the side)")