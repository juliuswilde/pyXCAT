from pathlib import Path

from pydantic import BaseModel, Field

class CardiacParameters(BaseModel):

    heart_curve_file: Path = Field(default=Path("heart_curve.txt"), alias="heart_curve_file", description="name for file containing time curve for heart")
