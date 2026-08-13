from pathlib import Path

from pydantic import BaseModel, Field

class ActivityParameters(BaseModel):

    use_activ_material_table: bool = Field(default=False, alias="use_activ_material_table", description="use table to define organ activities and/or materials for attenuation")
    activ_material_table_filename: Path = Field(default=Path("activ_material_table.txt"), alias="activ_material_table_filename", description="name of table file to use for the above\n#\tTable can define values for new user objects or alter values for existing objects\n#\tValues are set in the table like this:\n#\tobject_name	activity_value	materials_separated_by_commas	material_fractions_separated_by_commas\n#\tMesh objects require 'tmod_' to be at the beginning of the name.  The file 'activ_material_table.txt' provides an example for the table.")
    