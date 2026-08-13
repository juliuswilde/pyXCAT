from pathlib import Path

from pydantic import BaseModel, Field

class RespirationParameters(BaseModel):

    dia_filename: Path = Field(default=Path("diaphragm_curve.dat"), alias="dia_filename", description="name of curve defining diaphragm motion during respiration")
    ap_filename: Path = Field(default=Path("ap_curve.dat"), alias="ap_filename", description="name of curve defining chest anterior-posterior motion during respiration")
