import logging
import re
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from pyxcat.parameter_sets import *

logger = logging.getLogger(__name__)

# XCAT .par files line the trailing "# description" comments up on a fixed column,
# padded with hard tabs (see e.g. general_samp_GI_motility.par).
COMMENT_COLUMN = 44
TAB_WIDTH = 4

# Section banners are "#" + 20 dashes + title + 27 dashes, and the same banner is
# repeated unchanged as the closing line of the section.
SECTION_LEAD_DASHES = 20
SECTION_TRAIL_DASHES = 27

# Section title each parameter set is written under, in file order.
SECTION_TITLES = {
    "image_params": "Image dimensions",
    "body_params": "Body Setup",
    "respiration_params": "Respiration setup",
    "cardiac_params": "Cardiac",
    "lesion_params": "Lesion",
    "activity_params": "Activity Setup and Values",
    "attenuation_params": "Attenuation Setup",
    "gi_motility_params": "GI Motility Parameters",
    "user_object_params": "User object",
}

# Filenames XCAT only opens when the flag next to them is switched on. They keep
# their placeholder name (and are not checked for existence) while it is off.
GATED_PATHS = {
    "user_objects_file": "read_user_objects",
    "activ_material_table_filename": "use_activ_material_table",
    "tumor_motion_filename": "tumor_motion_flag",
    "tumor_rotation_filename": "tumor_rotation_flag",
}


class XCATParameters(BaseModel):
    activity_params: ActivityParameters = Field(default_factory=ActivityParameters)
    attenuation_params: AttenuationParameters = Field(default_factory=AttenuationParameters)
    body_params: BodyParameters = Field(default_factory=BodyParameters)
    cardiac_params: CardiacParameters = Field(default_factory=CardiacParameters)
    image_params: ImageParameters = Field(default_factory=ImageParameters)
    lesion_params: LesionParameters = Field(default_factory=LesionParameters)
    respiration_params: RespirationParameters = Field(default_factory=RespirationParameters)
    gi_motility_params: GIMotilityParameters = Field(default_factory=GIMotilityParameters)
    user_object_params: UserObjectParameters = Field(default_factory=UserObjectParameters)

    @classmethod
    def from_par(cls, path_to_par_file: Path):
        defaults = XCATParameters()

        for key, value in iter(defaults):
            extracted = extract_paremter_set_from_par(path_to_par_file, value)
            setattr(defaults, key, extracted)

        return defaults

    @classmethod
    def from_json(cls, path_to_json_file: Path):
        raise NotImplementedError

    def save_as_par(self, save_path: Path):
        self.resolve_all_paths()
        sections = [
            _format_section(SECTION_TITLES[name], getattr(self, name))
            for name in SECTION_TITLES
        ]

        with open(save_path, "w") as f:
            f.write("\n\n".join(sections) + "\n")
            f.write(parameter_notes)

    def save_as_json(self, save_path: Path):
        raise NotImplementedError

    def resolve_all_paths(self):
        for key, value in iter(self):
            if isinstance(value, Path):
                resolved = value.resolve()
                if not resolved.is_file():
                    raise FileNotFoundError(f"{key}: {value} could not be found (resolved to: {resolved})")
                setattr(self, key, resolved)

            if issubclass(type(value), BaseModel):
                for nested_key, nested_value in iter(value):
                    if not isinstance(nested_value, Path):
                        continue

                    # XCAT never opens these unless their flag is set, so an
                    # unreadable placeholder name is fine while it is off.
                    gate = GATED_PATHS.get(nested_key)
                    if gate is not None and not getattr(value, gate):
                        continue

                    resolved = nested_value.resolve()
                    if not resolved.is_file():
                        raise FileNotFoundError(f"{key}.{nested_key}: {nested_value} could not be found (resolved to: {resolved})")
                    setattr(value, nested_key, resolved)


def _format_section(title: str, params: BaseModel) -> str:
    banner = (
        "#" + "-" * SECTION_LEAD_DASHES + title + "-" * SECTION_TRAIL_DASHES
    )

    lines = [banner]
    for name, field in type(params).model_fields.items():
        key = field.alias or name
        lines.append(_format_line(key, getattr(params, name), field.description))
    lines.append(banner)

    return "\n".join(lines)


def _format_line(key: str, value: Any, description: str | None) -> str:
    entry = f"{key} = {_format_value(value)}"

    if not description:
        return entry

    # ceil division, so the comment always clears the entry by at least one tab
    tabs = max(1, -(-(COMMENT_COLUMN - len(entry)) // TAB_WIDTH))
    return entry + "\t" * tabs + f"# {description}"


def _format_value(value: Any) -> str:
    if isinstance(value, bool):
        return "1" if value else "0"
    return str(value)

def extract_paremter_set_from_par(path_to_par: Path, parameter_set: BaseModel):
    if not path_to_par.exists() or not path_to_par.suffix == ".par":
        raise FileNotFoundError(f"No parameter file at: {path_to_par}")
    with open(path_to_par, "r") as f:
        parameter_file = f.read()

    values: dict[str, str] = {}
    for key, _ in iter(parameter_set):
        match = re.search(rf"^{re.escape(key)}\s*=\s*(.+?)\s*(?:#.*)?$", parameter_file, re.MULTILINE)
        # A missing entry is not an error: XCAT itself falls back to a built-in
        # default, and no par file in circulation lists all 377 parameters. Keep
        # the field default so the same value is written back out.
        if match is None:
            logger.debug("Parameter '%s' not found in %s, keeping default", key, path_to_par)
            continue
        values[key] = match.group(1)

    return type(parameter_set)(**values)
