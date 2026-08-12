from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field

from pyxcat.parameter_sets import ImageParameters, BodyParameters

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
    "body_params": "Body Setup"
}


class XCATParameters(BaseModel):

    image_params: ImageParameters = Field(default_factory=ImageParameters)
    body_params: BodyParameters = Field(default_factory=BodyParameters)

    @classmethod
    def from_par(cls, path_to_par_file: Path):
        pass

    @classmethod
    def from_json(cls, path_to_json_file: Path):
        pass

    def save_as_par(self, save_path: Path):
        sections = [
            _format_section(SECTION_TITLES[name], getattr(self, name))
            for name in SECTION_TITLES
        ]

        with open(save_path, "w") as f:
            f.write("\n\n".join(sections) + "\n")

    def save_as_json(self, save_path: Path):
        pass


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
