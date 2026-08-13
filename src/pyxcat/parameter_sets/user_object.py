from pathlib import Path

from pydantic import BaseModel, Field


class UserObjectParameters(BaseModel):
    """User-defined NURBS surfaces added to the phantom; see NOTE 13.

    When enabled, ``ActivityParameters.use_activ_material_table`` must also be set and
    the activity/material table must define the new objects.
    """

    read_user_objects: bool = Field(default=False, alias="read_user_objects", description="read a user-defined surface file (0 = no, 1 = yes)")
    user_objects_file: Path = Field(default=Path("user_objects.nrb"), alias="user_objects_file", description="filename of the user-defined surface file")
    deformation_flag: bool = Field(default=False, alias="deformation_flag", description="deformation of user objects with motion (0 = rigid, 1 = non-rigid)")

    num_for_user_vectors: int = Field(default=50, ge=1, alias="num_for_user_vectors", description="number of sample points used per user object when writing motion vectors in mode 4")
