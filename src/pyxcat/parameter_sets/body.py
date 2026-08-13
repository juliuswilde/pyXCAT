from pathlib import Path

from pydantic import BaseModel, Field


class BodyParameters(BaseModel):
    """Anatomy of the phantom: which body model is loaded, how it is scaled, and
    the wall/organ dimensions that are derived from it."""

    ### Base anatomy ###
    gender: int = Field(default=0, ge=0, le=1, alias="gender", description="male or female phantom (0 = male, 1 = female), be sure to adjust below accordingly")

    organ_file: Path = Field(default=Path("vmale50.nrb"), alias="organ_file", description="name of organ file that defines all organs (male = vmale50.nrb, female = vfemale50.nrb)")
    heart_base: Path = Field(default=Path("vmale50_heart.nrb"), alias="heart_base", description="basename for heart files (male = vmale50_heart.nrb; female = vfemale50_heart.nrb)")

    vessel_flag: bool = Field(default=False, alias="vessel_flag", description="vessel_flag (1 = include arteries and veins, 0 = do not include)")
    arms_flag: bool = Field(default=False, alias="arms_flag", description="arms_flag (0 = no arms, 1 = arms at the side)")
    iodine_flag: bool = Field(default=False, alias="iodine_flag", description="iodine_flag (1 = set blood to have iodine contrast, 0 = do not use contrast)")

    marrow_flag: bool = Field(default=False, alias="marrow_flag", description="render marrow (0 = no, 1 = yes)")
    yellow_marrow_flag: bool = Field(default=False, alias="yellow_marrow_flag", description="yellow_marrow_flag (1 = include yellow marrow, 0 = do not)")

    frac_H2O: float = Field(default=0.5, ge=0.0, le=1.0, alias="frac_H2O", description="fraction (by weight) of water in wet bone and wet spine (used to calc. atten coeff)")
    thickness_skin: float = Field(default=0.0, ge=0.0, alias="thickness_skin", description="thickness of the skin (cm), if greater than 0, it adds a skin layer to the body")

    lung_scale: float = Field(default=1.0, gt=0.0, alias="lung_scale", description="lung_scale (value to scale the lungs from 0 to 1)")

    ### Whole phantom placement and scaling ###
    phan_rotx: float = Field(default=0.0, alias="phan_rotx", description="degree to rotate the entire phantom by the x-axis")
    phan_roty: float = Field(default=0.0, alias="phan_roty", description="degree to rotate the entire phantom by the y-axis")
    phan_rotz: float = Field(default=0.0, alias="phan_rotz", description="degree to rotate the entire phantom by the z-axis")

    phantom_long_axis_scale: float = Field(default=1.0, gt=0.0, alias="phantom_long_axis_scale", description="phantom_long_axis_scale (scales phantom laterally - scales everything including the heart) SEE NOTE 5")
    phantom_short_axis_scale: float = Field(default=1.0, gt=0.0, alias="phantom_short_axis_scale", description="phantom_short_axis_scale (scales phantom AP - scales everything including the heart) SEE NOTE 5")
    phantom_height_scale: float = Field(default=1.0, gt=0.0, alias="phantom_height_scale", description="phantom_height_scale (scales phantom height - scales everything including the heart) SEE NOTE 5")

    ### Head ###
    head_x_scale: float = Field(default=1.0, gt=0.0, alias="head_x_scale", description="head_x_scale (scales head laterally - scales everything in head) SEE NOTE 5")
    head_y_scale: float = Field(default=1.0, gt=0.0, alias="head_y_scale", description="head_y_scale (scales head about AP - scales everything in head) SEE NOTE 5")
    head_height_scale: float = Field(default=1.0, gt=0.0, alias="head_height_scale", description="head_height_scale (scales head height - scales everything in head) SEE NOTE 5")
    head_skin_x_scale: float = Field(default=1.0, gt=0.0, alias="head_skin_x_scale", description="head_skin_x_scale (scales head laterally - scales only outer skin) SEE NOTE 5")
    head_skin_y_scale: float = Field(default=1.0, gt=0.0, alias="head_skin_y_scale", description="head_skin_y_scale (scales head about AP - scales only outer skin) SEE NOTE 5")

    ### Torso ###
    torso_long_axis_scale: float = Field(default=1.0, gt=0.0, alias="torso_long_axis_scale", description="torso_long_axis_scale (sets torso, chest and abdomen, transverse axis - scales everything including the heart) SEE NOTE 5")
    torso_short_axis_scale: float = Field(default=1.0, gt=0.0, alias="torso_short_axis_scale", description="torso_short_axis_scale (sets torso, chest and abdomen, AP axis - scales everything including the heart) SEE NOTE 5")

    chest_skin_long_axis_scale: float = Field(default=1.0, gt=0.0, alias="chest_skin_long_axis_scale", description="chest_skin_long_axis_scale (sets chest transverse axis - scales only body outline) SEE NOTE 5")
    chest_skin_short_axis_scale: float = Field(default=1.0, gt=0.0, alias="chest_skin_short_axis_scale", description="chest_skin_short_axis_scale (sets chest AP axis - scales only body outline) SEE NOTE 5")

    abdomen_skin_long_axis_scale: float = Field(default=1.0, gt=0.0, alias="abdomen_skin_long_axis_scale", description="abdomen_skin_long_axis_scale (sets abdomen transverse axis - scales only body outline) SEE NOTE 5")
    abdomen_skin_short_axis_scale: float = Field(default=1.0, gt=0.0, alias="abdomen_skin_short_axis_scale", description="abdomen_skin_short_axis_scale (sets abdomen AP axis - scales only body outline) SEE NOTE 5")

    pelvis_skin_long_axis_scale: float = Field(default=1.0, gt=0.0, alias="pelvis_skin_long_axis_scale", description="pelvis_skin_long_axis_scale (sets pelvis transverse axis - scales only body outline) SEE NOTE 5")
    pelvis_skin_short_axis_scale: float = Field(default=1.0, gt=0.0, alias="pelvis_skin_short_axis_scale", description="pelvis_skin_short_axis_scale (sets pelvis AP axis - scales only body outline) SEE NOTE 5")

    ### Limbs ###
    arms_cir_scale: float = Field(default=1.0, gt=0.0, alias="arms_cir_scale", description="arms_circumference_scale (scales arms radially - scales everything in arms) SEE NOTE 5")
    arms_length_scale: float = Field(default=1.0, gt=0.0, alias="arms_length_scale", description="arms_length_scale (scales arms length - scales everything in arms) SEE NOTE 5")
    arms_skin_cir_scale: float = Field(default=1.0, gt=0.0, alias="arms_skin_cir_scale", description="arms_skin_circumference_scale (scales arms radially - scales only outer skin) SEE NOTE 5")

    legs_cir_scale: float = Field(default=1.0, gt=0.0, alias="legs_cir_scale", description="legs_circumference_scale (scales legs radially - scales everything in legs) SEE NOTE 5")
    legs_length_scale: float = Field(default=1.0, gt=0.0, alias="legs_length_scale", description="legs_length_scale (scales legs length - scales everything in legs) SEE NOTE 5")
    legs_skin_cir_scale: float = Field(default=1.0, gt=0.0, alias="legs_skin_cir_scale", description="legs_skin_circumference_scale (scales legs radially - scales only outer skin) SEE NOTE 5")

    ### Bones and muscle ###
    bones_scale: float = Field(default=1.0, gt=0.0, alias="bones_scale", description="bones_scale (scales all bones in 2D about their centerlines, makes each bone thicker) SEE NOTE 5")

    head_torso_muscle_scale: float = Field(default=1.0, gt=0.0, alias="head_torso_muscle_scale", description="head_torso_muscle_scale (compresses/expands the muscles radially) SEE NOTE 5")
    arms_muscle_cir_scale: float = Field(default=1.0, gt=0.0, alias="arms_muscle_cir_scale", description="arms_muscle_cir_scale (compresses/expands the muscles radially) SEE NOTE 5")
    legs_muscle_cir_scale: float = Field(default=1.0, gt=0.0, alias="legs_muscle_cir_scale", description="legs_muscle_cir_scale (compresses/expands the muscles radially) SEE NOTE 5")

    ### Breasts ###
    breast_type: int = Field(default=1, ge=0, le=1, alias="breast_type", description="breast_type (0=supine, 1=prone)")
    which_breast: int = Field(default=0, ge=0, le=3, alias="which_breast", description="which_breast (0 = none, 1 = both, 2 = right only, 3 = left only)")

    breast_to_compress: int = Field(default=0, ge=0, le=3, alias="breast_to_compress", description="breast to apply compression (0 = none, 1 = right, 2 = left, 3 = both)")
    compression_type: int = Field(default=0, ge=0, le=1, alias="compression_type", description="type of compression (0 = top/bottom, 1 = side to side)")
    compression_factor: float = Field(default=0.5, ge=0.0, le=1.0, alias="compression_factor", description="factor to compress breast by (0 full compression - 1 no compression)")

    rbreast_long_axis_scale: float = Field(default=1.0, gt=0.0, alias="rbreast_long_axis_scale", description="right breast_long_axis (sets the breasts lateral dimension) SEE NOTE 5")
    rbreast_short_axis_scale: float = Field(default=1.0, gt=0.0, alias="rbreast_short_axis_scale", description="right breast_short_axis (sets the breasts antero-posterior dimension) SEE NOTE 5")
    rbreast_height_scale: float = Field(default=1.0, gt=0.0, alias="rbreast_height_scale", description="right breast_height (sets the breasts height) SEE NOTE 5")
    vol_rbreast: float = Field(default=0.0, ge=0.0, alias="vol_rbreast", description="sets rbreast volume by scaling in 3D, will over-rule above scalings")
    rbr_theta: float = Field(default=0.0, alias="rbr_theta", description="theta angle of the right breast (angle the breast is tilted transversely (sideways) from the center of the chest) SEE NOTE 5")
    rbr_phi: float = Field(default=0.0, alias="rbr_phi", description="phi angle of the right breast (angle the breast is tilted up (+) or down (-)) SEE NOTE 5")
    r_br_tx: float = Field(default=0.0, alias="r_br_tx", description="x translation for right breast")
    r_br_ty: float = Field(default=0.0, alias="r_br_ty", description="y translation for right breast")
    r_br_tz: float = Field(default=0.0, alias="r_br_tz", description="z translation for right breast")

    lbreast_long_axis_scale: float = Field(default=1.0, gt=0.0, alias="lbreast_long_axis_scale", description="left breast_long_axis (sets the breasts lateral dimension) SEE NOTE 5")
    lbreast_short_axis_scale: float = Field(default=1.0, gt=0.0, alias="lbreast_short_axis_scale", description="left breast_short_axis (sets the breasts antero-posterior dimension) SEE NOTE 5")
    lbreast_height_scale: float = Field(default=1.0, gt=0.0, alias="lbreast_height_scale", description="left breast_height (sets the breasts height) SEE NOTE 5")
    vol_lbreast: float = Field(default=0.0, ge=0.0, alias="vol_lbreast", description="sets lbreast volume by scaling in 3D, will over-rule above scalings")
    lbr_theta: float = Field(default=0.0, alias="lbr_theta", description="theta angle of the left breast (angle the breast is tilted transversely (sideways) from the center of the chest) SEE NOTE 5")
    lbr_phi: float = Field(default=0.0, alias="lbr_phi", description="phi angle of the left breast (angle the breast is tilted up (+) or down (-)) SEE NOTE 5")
    l_br_tx: float = Field(default=0.0, alias="l_br_tx", description="x translation for left breast")
    l_br_ty: float = Field(default=0.0, alias="l_br_ty", description="y translation for left breast")
    l_br_tz: float = Field(default=0.0, alias="l_br_tz", description="z translation for left breast")

    ### Diaphragm domes ###
    rdiaph_liv_scale: float = Field(default=1.0, ge=0.0, alias="rdiaph_liv_scale", description="height of right_diaphragm/liver dome (0 = flat, 1 = original height, > 1 raises the diaphragm) SEE NOTE 5")
    ldiaph_scale: float = Field(default=1.0, ge=0.0, alias="ldiaph_scale", description="height of left diaphragm dome (0 = flat, 1 = original height, > 1 raises the diaphragm) SEE NOTE 5")

    ### Bone thicknesses (cm) ###
    thickness_skull: float = Field(default=0.2, gt=0.0, alias="thickness_skull", description="thickness skull (cm)")
    thickness_mandible: float = Field(default=0.3, gt=0.0, alias="thickness_mandible", description="thickness mandible (cm)")
    thickness_sternum: float = Field(default=0.4, gt=0.0, alias="thickness_sternum", description="thickness sternum (cm)")
    thickness_scapula: float = Field(default=0.35, gt=0.0, alias="thickness_scapula", description="thickness scapulas (cm)")
    thickness_ribs: float = Field(default=0.3, gt=0.0, alias="thickness_ribs", description="thickness ribs (cm)")
    thickness_backbone: float = Field(default=0.4, gt=0.0, alias="thickness_backbone", description="thickness backbone (cm)")
    thickness_pelvis: float = Field(default=0.4, gt=0.0, alias="thickness_pelvis", description="thickness pelvis (cm)")
    thickness_collar: float = Field(default=0.35, gt=0.0, alias="thickness_collar", description="thickness collarbones (cm)")
    thickness_humerus: float = Field(default=0.45, gt=0.0, alias="thickness_humerus", description="thickness humerus (cm)")
    thickness_radius: float = Field(default=0.45, gt=0.0, alias="thickness_radius", description="thickness radius (cm)")
    thickness_ulna: float = Field(default=0.45, gt=0.0, alias="thickness_ulna", description="thickness ulna (cm)")
    thickness_hand: float = Field(default=0.35, gt=0.0, alias="thickness_hand", description="thickness hand bones (cm)")
    thickness_femur: float = Field(default=0.5, gt=0.0, alias="thickness_femur", description="thickness femur (cm)")
    thickness_tibia: float = Field(default=0.6, gt=0.0, alias="thickness_tibia", description="thickness tibia (cm)")
    thickness_fibula: float = Field(default=0.5, gt=0.0, alias="thickness_fibula", description="thickness fibula (cm)")
    thickness_patella: float = Field(default=0.3, gt=0.0, alias="thickness_patella", description="thickness patella (cm)")
    thickness_foot: float = Field(default=0.4, gt=0.0, alias="thickness_foot", description="thickness foot bones (cm)")
    thickness_sacrum: float = Field(default=0.25, gt=0.0, alias="thickness_sacrum", description="thickness sacrum (cm)")

    ### GI tract wall thicknesses (cm) ###
    thickness_si: float = Field(default=0.6, gt=0.0, alias="thickness_si", description="thickness of small intestine wall (cm)")
    thickness_li: float = Field(default=0.6, gt=0.0, alias="thickness_li", description="thickness of large intestine wall (cm)")
    si_air_flag: bool = Field(default=False, alias="si_air_flag", description="0 = do not include air and 1 = include air in small intestine")
    li_air_flag: int = Field(default=0, ge=0, le=5, alias="li_air_flag", description="location of air in the large intestine see NOTE 6")

    thickness_stomach: float = Field(default=0.7, gt=0.0, alias="thickness_stomach", description="thickness of stomach wall (cm)")
    thickness_esoph: float = Field(default=0.3, gt=0.0, alias="thickness_esoph", description="thickness of the esophagus wall (cm)")
    thickness_trachea: float = Field(default=0.15, gt=0.0, alias="thickness_trachea", description="thickness of the trachea wall (cm)")

    ### Kidney cortex ###
    rkidney_thickness: float = Field(default=-1.0, alias="rkidney_thickness", description="rkidney cortex thickness (value < 0 = do not change, 0.0 = set uniform cortex thickness based on average calculated from kidney, value > 0 sets the uniform thickness in mm's)")
    lkidney_thickness: float = Field(default=-1.0, alias="lkidney_thickness", description="lkidney cortex thickness (value < 0 = do not change, 0.0 = set uniform cortex thickness based on average calculated from kidney, value > 0 sets the uniform thickness in mm's)")

    ### Prostate placement ###
    prostate_transx: float = Field(default=0.0, alias="prostate_transx", description="x translation for the prostate")
    prostate_transy: float = Field(default=0.0, alias="prostate_transy", description="y translation for the prostate")
    prostate_transz: float = Field(default=0.0, alias="prostate_transz", description="z translation for the prostate")

    ### Brain lymphatic vessels (undocumented in the sample par file) ###
    brain_lymph_vess_flag: bool = Field(default=False, alias="brain_lymph_vess_flag", description="brain lymphatic vessel flag (1 = include the sagittal sinus lymphatic vessels, 0 = do not include)")
    sag_sinus_lymph_vess_right_diameter: float = Field(default=0.1, gt=0.0, alias="sag_sinus_lymph_vess_right_diameter", description="diameter of the right sagittal sinus lymphatic vessel")
    sag_sinus_lymph_vess_left_diameter: float = Field(default=0.1, gt=0.0, alias="sag_sinus_lymph_vess_left_diameter", description="diameter of the left sagittal sinus lymphatic vessel")
    sag_sinus_lymph_vess_bottom_diameter: float = Field(default=0.1, gt=0.0, alias="sag_sinus_lymph_vess_bottom_diameter", description="diameter of the bottom sagittal sinus lymphatic vessel")
    sag_sinus_lymph_vess_right_offset: float = Field(default=0.0, alias="sag_sinus_lymph_vess_right_offset", description="offset of the right sagittal sinus lymphatic vessel from the sinus")
    sag_sinus_lymph_vess_left_offset: float = Field(default=0.0, alias="sag_sinus_lymph_vess_left_offset", description="offset of the left sagittal sinus lymphatic vessel from the sinus")
    sag_sinus_lymph_vess_bottom_offset: float = Field(default=0.0, alias="sag_sinus_lymph_vess_bottom_offset", description="offset of the bottom sagittal sinus lymphatic vessel from the sinus")

    ### Organ volumes (mL); 0 = do not change ###
    vol_prostate: float = Field(default=0.0, ge=0.0, alias="vol_prostate", description="set the volume of the prostate; (0 = do not change)")
    vol_testes: float = Field(default=0.0, ge=0.0, alias="vol_testes", description="set the volume of the testes; (0 = do not change)")
    vol_epidy: float = Field(default=0.0, ge=0.0, alias="vol_epidy", description="set the volume of the epididymus; (0 = do not change)")
    vol_liver: float = Field(default=0.0, ge=0.0, alias="vol_liver", description="set the volume of the liver; (0 = do not change)")
    vol_gall_bladder: float = Field(default=0.0, ge=0.0, alias="vol_gall_bladder", description="set the volume of the gall_bladder; (0 = do not change)")
    vol_stomach: float = Field(default=0.0, ge=0.0, alias="vol_stomach", description="set the volume of the stomach; (0 = do not change)")
    vol_pancreas: float = Field(default=0.0, ge=0.0, alias="vol_pancreas", description="set the volume of the pancreas; (0 = do not change)")
    vol_spleen: float = Field(default=0.0, ge=0.0, alias="vol_spleen", description="set the volume of the spleen; (0 = do not change)")
    vol_rkidney: float = Field(default=0.0, ge=0.0, alias="vol_rkidney", description="set the volume of the right kidney; (0 = do not change)")
    vol_lkidney: float = Field(default=0.0, ge=0.0, alias="vol_lkidney", description="set the volume of the left kidney; (0 = do not change)")
    vol_radrenal: float = Field(default=0.0, ge=0.0, alias="vol_radrenal", description="set the volume of the right adrenal; (0 = do not change)")
    vol_ladrenal: float = Field(default=0.0, ge=0.0, alias="vol_ladrenal", description="set the volume of the left adrenal; (0 = do not change)")
    vol_small_intest: float = Field(default=0.0, ge=0.0, alias="vol_small_intest", description="set the volume of the small intestine; (0 = do not change)")
    vol_large_intest: float = Field(default=0.0, ge=0.0, alias="vol_large_intest", description="set the volume of the large intestine; (0 = do not change)")
    vol_bladder: float = Field(default=0.0, ge=0.0, alias="vol_bladder", description="set the volume of the bladder; (0 = do not change)")
    vol_rthyroid: float = Field(default=0.0, ge=0.0, alias="vol_rthyroid", description="set the volume of the right thyroid; (0 = do not change)")
    vol_lthyroid: float = Field(default=0.0, ge=0.0, alias="vol_lthyroid", description="set the volume of the left thyroid; (0 = do not change)")
    vol_thymus: float = Field(default=0.0, ge=0.0, alias="vol_thymus", description="set the volume of the thymus; (0 = do not change)")
    vol_salivary: float = Field(default=0.0, ge=0.0, alias="vol_salivary", description="set the volume of the salivary glands; (0 = do not change)")
    vol_pituitary: float = Field(default=0.0, ge=0.0, alias="vol_pituitary", description="set the volume of the pituitary gland; (0 = do not change)")
    vol_eyes: float = Field(default=0.0, ge=0.0, alias="vol_eyes", description="set the volume of the eyes; (0 = do not change)")
    vol_rovary: float = Field(default=0.0, ge=0.0, alias="vol_rovary", description="set the volume of the right ovary; (0 = do not change)")
    vol_lovary: float = Field(default=0.0, ge=0.0, alias="vol_lovary", description="set the volume of the left ovary; (0 = do not change)")
    vol_ftubes: float = Field(default=0.0, ge=0.0, alias="vol_ftubes", description="set the volume of the fallopian tubes; (0 = do not change)")
    vol_uterus: float = Field(default=0.0, ge=0.0, alias="vol_uterus", description="set the volume of the uterus; (0 = do not change)")
    vol_vagina: float = Field(default=0.0, ge=0.0, alias="vol_vagina", description="set the volume of the vagina; (0 = do not change)")
    vol_larynx: float = Field(default=0.0, ge=0.0, alias="vol_larynx", description="set the volume of the larynx/pharynx; (0 = do not change)")
    vol_trachea: float = Field(default=0.0, ge=0.0, alias="vol_trachea", description="set the volume of the trachea (total); (0 = do not change)")
    vol_esoph: float = Field(default=0.0, ge=0.0, alias="vol_esoph", description="set the volume of the esophagus (total); (0 = do not change)")
