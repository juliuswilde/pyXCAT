from typing import Literal

from pydantic import BaseModel, Field


class GIMotilityParameters(BaseModel):
    """Gastrointestinal motility model.

    The executable returns a flat 0.1 (or 1.0) for every parameter in this block when
    it is missing, which is a generic fallback rather than a physiologically usable
    value. The defaults below are taken from the sample parameter file instead.
    """

    GI_motion_flag: int = Field(default=0, ge=0, le=4, alias="GI_motion_flag", description="GI motility mode to include (0 = none, 1 = peristalsis, 2 = rhythmic segmentation, 3 = high-amplitude propagating contraction, 4 = tonic contraction)")
    which_organ: int = Field(default=3, ge=1, le=5, alias="which_organ", description="organ to include motion (1 = esophagus, 2 = stomach, 3 = small intestine, 4 = large intestine, 5 = rectum)")

    ### Dispersion ###
    alpha_space: float = Field(default=0.0, ge=0.0, alias="alpha_space", description="spatial dispersion for motion")
    alpha_time: float = Field(default=0.0, ge=0.0, alias="alpha_time", description="temporal dispersion for motion")
    dispersion_mode_space: Literal["lin", "exp", "pow"] = Field(default="lin", alias="dispersion_mode_space", description="mode for spatial dispersion; lin=linear, exp=exponential, pow=inverse power law")
    dispersion_mode_time: Literal["lin", "exp", "pow"] = Field(default="lin", alias="dispersion_mode_time", description="mode for temporal dispersion; lin=linear, exp=exponential, pow=inverse power law")

    ### Peristalsis (GI_motion_flag = 1) ###
    peristalsis_WaveAmplitude: float = Field(default=5.0, ge=0.0, alias="peristalsis_WaveAmplitude", description="wave amplitude for peristalsis motion (mm)")
    peristalsis_WaveLength: float = Field(default=100.0, gt=0.0, alias="peristalsis_WaveLength", description="wave length for peristalsis motion (mm)")
    peristalsis_WaveSpeed: float = Field(default=10.0, gt=0.0, alias="peristalsis_WaveSpeed", description="wave speed for peristalsis motion (mm/sec)")

    ### Rhythmic segmentation (GI_motion_flag = 2) ###
    rhythmic_seg_WaveAmplitude: float = Field(default=0.5, ge=0.0, alias="rhythmic_seg_WaveAmplitude", description="wave amplitude for rhythmic segmentation motion (mm)")
    rhythmic_seg_NodalPoints: float = Field(default=5.0, ge=2.0, alias="rhythmic_seg_NodalPoints", description="number of nodes, including the stationary endpoints, in the standing wave")
    rhythmic_seg_WaveSpeed: float = Field(default=0.5, gt=0.0, alias="rhythmic_seg_WaveSpeed", description="wave speed for rhythmic segmentation motion (mm/sec)")

    ### High-amplitude propagating contractions (GI_motion_flag = 3) ###
    HAPCs_BolusSize: float = Field(default=0.5, gt=0.0, alias="HAPCs_BolusSize", description="parameter to control the size of the traveling bolus (mm)")
    HAPCs_WaveAmplitude: float = Field(default=0.5, ge=0.0, alias="HAPCs_WaveAmplitude", description="wave amplitude for high-amplitude propagating contraction motion (mm)")
    HAPCs_WaveSpeed: float = Field(default=0.5, gt=0.0, alias="HAPCs_WaveSpeed", description="wave speed for high-amplitude propagating contraction motion (mm/sec)")

    ### Tonic contractions (GI_motion_flag = 4) ###
    tonic_contractions_tcAmplitude: float = Field(default=0.5, ge=0.0, alias="tonic_contractions_tcAmplitude", description="amplitude of tonic contraction (mm)")
    tonic_contractions_tcLocation: float = Field(default=0.5, ge=0.0, alias="tonic_contractions_tcLocation", description="location of TC specified along the length of organ (mm); 0 = TC at beginning of organ")
    tonic_contractions_tcSize: float = Field(default=0.5, gt=0.0, alias="tonic_contractions_tcSize", description="parameter to control the size (along the length of organ) of the tonic contraction (mm)")
    tonic_contractions_tcTime: float = Field(default=0.01, ge=0.0, alias="tonic_contractions_tcTime", description="time at which the tonic contraction appears (sec)")
