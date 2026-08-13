from pathlib import Path

from pydantic import BaseModel, Field


class CardiacParameters(BaseModel):
    """Beating-heart model: cycle timing, the LV volume curve, heart scaling and
    the initial orientation of the LV long axis."""

    ### Cardiac cycle ###
    heart_curve_file: Path = Field(default=Path("heart_curve.txt"), alias="heart_curve_file", description="name for file containing time curve for heart")
    hrt_period: float = Field(default=1.0, gt=0.0, alias="hrt_period", description="hrt_period (SECS) (length of beating heart cycle; normal = 1s) see NOTE 3")
    hrt_start_ph_index: float = Field(default=0.0, ge=0.0, le=1.0, alias="hrt_start_ph_index", description="hrt_start_phase_index (range=0 to 1; ED=0, ES=0.4) see NOTE 3")

    ### Myocardium ###
    apical_thin: float = Field(default=0.0, ge=0.0, le=1.0, alias="apical_thin", description="apical_thinning (0 to 1.0 scale, 0.0 = not present, 0.5 = halfway present, 1.0 = completely thin)")
    uniform_heart: bool = Field(default=False, alias="uniform_heart", description="sets the thickness of the LV (0 = default, nonuniform wall thickness; 1 = uniform wall thickness for LV)")
    valve_thickness: float = Field(default=0.0, ge=0.0, alias="valve_thickness", description="thickness of the AV valves (cm);")

    ### Structures to include ###
    coronary_art_flag: bool = Field(default=False, alias="coronary_art_flag", description="coronary artery flag (1 = include coronary arteries, 0 = do not include)")
    coronary_vein_flag: bool = Field(default=False, alias="coronary_vein_flag", description="coronary vein flag (1 = include coronary veins, 0 = do not include)")
    papillary_flag: bool = Field(default=False, alias="papillary_flag", description="papillary_flag (1 = include papillary muscles in heart, 0 = do not include)")

    ### LV volume curve; see NOTE 3A ###
    hrt_v1: float = Field(default=0.0, ge=0.0, alias="hrt_v1", description="sets the LV end-diastolic volume (0 = do not change); see NOTE 3A")
    hrt_v2: float = Field(default=0.0, ge=0.0, alias="hrt_v2", description="sets the LV end-systolic volume (0 = do not change); see NOTE 3A")
    hrt_v3: float = Field(default=0.0, ge=0.0, alias="hrt_v3", description="sets the LV volume at the beginning of the quiet phase (0 = do not change); see NOTE 3A")
    hrt_v4: float = Field(default=0.0, ge=0.0, alias="hrt_v4", description="sets the LV volume at the end of the quiet phase (0 = do not change); see NOTE 3A")
    hrt_v5: float = Field(default=0.0, ge=0.0, alias="hrt_v5", description="sets the LV volume during reduced filling, before end-diastole (0 = do not change); see NOTE 3A")

    # hrt_t1 .. hrt_t4 are fractions of the cardiac cycle and must add up to 1.
    hrt_t1: float = Field(default=0.5, ge=0.0, le=1.0, alias="hrt_t1", description="sets the duration from end-diastole to end-systole, hrt_v1 to hrt_v2 (default = 0.5s); see NOTE 3A")
    hrt_t2: float = Field(default=0.192, ge=0.0, le=1.0, alias="hrt_t2", description="sets the duration from end-systole to beginning of quiet phase, hrt_v2 to hrt_v3 (default = 0.192s); see NOTE 3A")
    hrt_t3: float = Field(default=0.115, ge=0.0, le=1.0, alias="hrt_t3", description="sets the duration of quiet phase, hrt_v3 to hrt_v4 (default = 0.115s); see NOTE 3A")
    hrt_t4: float = Field(default=0.193, ge=0.0, le=1.0, alias="hrt_t4", description="sets the duration from end of quiet phase to reduced filling, hrt_v4 to hrt_v5 (default = 0.193s); see NOTE 3A")

    ### Heart scaling ###
    hrt_scale_x: float = Field(default=1.0, gt=0.0, alias="hrt_scale_x", description="hrt_scale x")
    hrt_scale_y: float = Field(default=1.0, gt=0.0, alias="hrt_scale_y", description="hrt_scale y")
    hrt_scale_z: float = Field(default=1.0, gt=0.0, alias="hrt_scale_z", description="hrt_scale z")

    lv_radius_scale: float = Field(default=1.0, gt=0.0, alias="lv_radius_scale", description="lv_radius_scale (value from 0 to 1 to scale the radius of the left ventricle)")
    lv_length_scale: float = Field(default=1.0, gt=0.0, alias="lv_length_scale", description="lv_length_scale (value from 0 to 1 to scale the length of the left ventricle)")

    ### Initial LV long-axis orientation and placement; see NOTE 8 ###
    d_ZY_rotation: float = Field(default=0.0, alias="d_ZY_rotation", description="change in zy_rotation (beta) in deg. (0); see NOTE 8")
    d_XZ_rotation: float = Field(default=0.0, alias="d_XZ_rotation", description="change in xz_rotation ( phi) in deg. (0);")
    d_YX_rotation: float = Field(default=0.0, alias="d_YX_rotation", description="change in yx_rotation ( psi) in deg. (0);")

    X_tr: float = Field(default=0.0, alias="X_tr", description="x translation in mm ;")
    Y_tr: float = Field(default=0.0, alias="Y_tr", description="y translation in mm ;")
    Z_tr: float = Field(default=0.0, alias="Z_tr", description="z translation in mm ;")
