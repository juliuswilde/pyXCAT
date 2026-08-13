from pathlib import Path

from pydantic import BaseModel, Field

class AttenuationParameters(BaseModel):

    energy: float = Field(default=120.0, ge=0.5, le=40000.0, alias="energy", description="radionuclide energy in keV (range 1 - 40MeV, increments of 0.5 keV) ; for attn. map only")
    atten_table_filename: Path = Field(default=Path("atten_table.dat"), alias="atten_table_filename", description="for attenuation data calculation")
