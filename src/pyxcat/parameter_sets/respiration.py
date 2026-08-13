from pathlib import Path

from pydantic import BaseModel, Field


class RespirationParameters(BaseModel):
    """Respiratory motion: the breathing cycle itself, the lung density model and
    the extent by which the heart and kidneys are dragged along by the diaphragm."""

    ### Breathing cycle ###
    resp_period: float = Field(default=5.0, gt=0.0, alias="resp_period", description="resp_period (SECS) (length of respiratory cycle; normal breathing = 5s) see NOTE 3")
    resp_start_ph_index: float = Field(default=0.0, ge=0.0, le=1.0, alias="resp_start_ph_index", description="resp_start_phase_index (range=0 to 1, full exhale=0.0, full inhale=0.4) see NOTE 3")

    max_diaphragm_motion: float = Field(default=2.0, ge=0.0, alias="max_diaphragm_motion", description="max_diaphragm_motion (extent in cm's of diaphragm motion; normal breathing = 2 cm) see NOTE 4")
    max_AP_exp: float = Field(default=0.5, ge=0.0, alias="max_AP_exp", description="max_AP_expansion (extent in cm's of the AP expansion of the chest; normal breathing = 1.2 cm) see NOTE 4")

    dia_filename: Path = Field(default=Path("diaphragm_curve.dat"), alias="dia_filename", description="name of curve defining diaphragm motion during respiration")
    ap_filename: Path = Field(default=Path("ap_curve.dat"), alias="ap_filename", description="name of curve defining chest anterior-posterior motion during respiration")

    ### User-supplied respiratory state (undocumented in the sample par file) ###
    # The exe rejects user_AP < 0 and user_DIA > 0: only inspiration states can be modified.
    user_resp_values: bool = Field(default=False, alias="user_resp_values", description="use the user supplied AP expansion / diaphragm motion below instead of the curve files (0 = no, 1 = yes)")
    user_AP: float = Field(default=0.0, ge=0.0, alias="user_AP", description="user defined AP expansion of the chest (cm); can only be >= 0 (can only modify inspiration states)")
    user_DIA: float = Field(default=0.0, le=0.0, alias="user_DIA", description="user defined diaphragm motion (cm); can only be <= 0 (can only modify inspiration states)")

    output_resp_log: bool = Field(default=False, alias="output_resp_log", description="save the respiratory movement of each frame to <out_base>_resp_movement.txt (0 = no, 1 = yes)")

    ### Lung density ###
    alter_lung_dens: bool = Field(default=False, alias="alter_lung_dens", description="alter_lung_dens (0 = keep lung density constant, 1 = change lung density with respiratory motion)")
    delta_lung_vol: float = Field(default=1500.0, ge=0.0, alias="delta_lung_vol", description="delta_lung_vol (amount of volume in mL's to add to end-expiration volume to set the baseline for 0.26 g/cm^3 inflated lung density)")

    ### Heart motion due to respiration ###
    hrt_motion_x: float = Field(default=0.0, alias="hrt_motion_x", description="hrt_motion_x (extent in cm's of the heart's LT/RT motion during breathing; default = 0.0 cm)")
    hrt_motion_y: float = Field(default=0.5, alias="hrt_motion_y", description="hrt_motion_y (extent in cm's of the heart's ANT/POST motion during breathing; default = 0.5 cm)")
    hrt_motion_z: float = Field(default=2.0, alias="hrt_motion_z", description="hrt_motion_z (extent in cm's of the heart's SUP/INF motion during breathing; default = 2.0 cm)")

    hrt_motion_rot_xz: float = Field(default=0.0, alias="hrt_motion_rot_xz", description="hrt_motion_rot_xz (extent in degrees of the heart's xz rotation during breathing; default = 0.0) SEE NOTE 4 and NOTE 8")
    hrt_motion_rot_yx: float = Field(default=0.0, alias="hrt_motion_rot_yx", description="hrt_motion_rot_yx (extent in degrees of the heart's yx rotation during breathing; default = 0.0) SEE NOTE 4 and NOTE 8")
    hrt_motion_rot_zy: float = Field(default=0.0, alias="hrt_motion_rot_zy", description="hrt_motion_rot_zy (extent in degrees of the heart's zy rotation during breathing; default = 0.0) SEE NOTE 4 and NOTE 8")

    ### Kidney motion due to respiration ###
    rkidney_motion_y: float = Field(default=0.5, alias="rkidney_motion_y", description="rkidney_motion_y (extent in cm's of the right kidney's AP motion during breathing; default = 0.5 cm)")
    rkidney_motion_z: float = Field(default=2.0, alias="rkidney_motion_z", description="rkidney_motion_z (extent in cm's of the right kidney's SUP/INF motion during breathing; default = 2.0 cm)")

    lkidney_motion_y: float = Field(default=0.5, alias="lkidney_motion_y", description="lkidney_motion_y (extent in cm's of the left kidney's AP motion during breathing; default = 0.5 cm)")
    lkidney_motion_z: float = Field(default=2.0, alias="lkidney_motion_z", description="lkidney_motion_z (extent in cm's of the left kidney's SUP/INF motion during breathing; default = 2.0 cm)")
