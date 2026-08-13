from pathlib import Path

from pydantic import BaseModel, Field


class ActivityParameters(BaseModel):
    """Activity value assigned to every structure of the activity phantom.

    The XCAT executable falls back to a flat 2.0 for *every* activity parameter it
    cannot find, which is a sentinel rather than a meaningful value. The defaults
    below are therefore taken from the sample parameter file instead.
    """

    activity_unit: int = Field(default=0, ge=0, le=1, alias="activity_unit", description="activity units (1= scale by voxel volume (multiply activity value times pixel_width * pixel_width * slice_width; 0= don't scale)")

    use_activ_material_table: bool = Field(default=False, alias="use_activ_material_table", description="use table to define organ activities and/or materials for attenuation")
    activ_material_table_filename: Path = Field(default=Path("activ_material_table.txt"), alias="activ_material_table_filename", description="name of table file to use for the above\n#\tTable can define values for new user objects or alter values for existing objects\n#\tValues are set in the table like this:\n#\tobject_name\tactivity_value\tmaterials_separated_by_commas\tmaterial_fractions_separated_by_commas\n#\tMesh objects require 'tmod_' to be at the beginning of the name.  The file 'activ_material_table.txt' provides an example for the table.")

    ### Heart ###
    myoLV_act: float = Field(default=7192.0, ge=0.0, alias="myoLV_act", description="hrt_myoLV_act - activity in left ventricle myocardium")
    myoRV_act: float = Field(default=7192.0, ge=0.0, alias="myoRV_act", description="hrt_myoRV_act - activity in right ventricle myocardium")
    myoLA_act: float = Field(default=7192.0, ge=0.0, alias="myoLA_act", description="hrt_myoLA_act - activity in left atrium myocardium")
    myoRA_act: float = Field(default=7192.0, ge=0.0, alias="myoRA_act", description="hrt_myoRA_act - activity in right atrium myocardium")
    bldplLV_act: float = Field(default=3102.0, ge=0.0, alias="bldplLV_act", description="hrt_bldplLV_act - activity in left ventricle chamber (blood pool)")
    bldplRV_act: float = Field(default=3102.0, ge=0.0, alias="bldplRV_act", description="hrt_bldplRV_act - activity in right ventricle chamber (blood pool)")
    bldplLA_act: float = Field(default=3102.0, ge=0.0, alias="bldplLA_act", description="hrt_bldplLA_act - activity in left atria chamber (blood pool)")
    bldplRA_act: float = Field(default=3102.0, ge=0.0, alias="bldplRA_act", description="hrt_bldplRA_act - activity in right atria chamber (blood pool)")
    coronary_art_activity: float = Field(default=7000.0, ge=0.0, alias="coronary_art_activity", description="coronary_art_activity - activity in the coronary arteries")
    coronary_vein_activity: float = Field(default=1000.0, ge=0.0, alias="coronary_vein_activity", description="coronary_vein_activity - activity in the coronary veins")
    pericardium_activity: float = Field(default=10000.0, ge=0.0, alias="pericardium_activity", description="pericardium activity;")

    ### Body and soft tissue ###
    body_activity: float = Field(default=42000.0, ge=0.0, alias="body_activity", description="body_activity (background activity);")
    skin_activity: float = Field(default=43000.0, ge=0.0, alias="skin_activity", description="skin_activity (used if skin_thickness is > 0)")
    muscle_activity: float = Field(default=12000.0, ge=0.0, alias="muscle_activity", description="muscle activity;")
    cartilage_activity: float = Field(default=3500.0, ge=0.0, alias="cartilage_activity", description="cartilage activity;")
    sinus_activity: float = Field(default=2.0, ge=0.0, alias="sinus_activity", description="sinus activity;")

    rbreast_activity: float = Field(default=40000.0, ge=0.0, alias="rbreast_activity", description="right breast activity;")
    lbreast_activity: float = Field(default=40000.0, ge=0.0, alias="lbreast_activity", description="left breast activity;")

    ### Airways and lungs ###
    r_lung_activity: float = Field(default=2500.0, ge=0.0, alias="r_lung_activity", description="right_lung_activity;")
    l_lung_activity: float = Field(default=2500.0, ge=0.0, alias="l_lung_activity", description="left_lung_activity;")
    trach_bronch_activity: float = Field(default=2500.0, ge=0.0, alias="trach_bronch_activity", description="trachea_bronchi_activity;")
    airway_activity: float = Field(default=2500.0, ge=0.0, alias="airway_activity", description="airway tree activity")
    laryngopharynx_activity: float = Field(default=10000.0, ge=0.0, alias="laryngopharynx_activity", description="laryngopharynx_activity")
    larynx_activity: float = Field(default=2000.0, ge=0.0, alias="larynx_activity", description="larynx_activity")

    ### Gastrointestinal tract ###
    esophagus_activity: float = Field(default=12000.0, ge=0.0, alias="esophagus_activity", description="esophagus_activity;")
    esophagus_cont_activity: float = Field(default=4000.0, ge=0.0, alias="esophagus_cont_activity", description="esophagus_contents_activity")
    st_wall_activity: float = Field(default=16000.0, ge=0.0, alias="st_wall_activity", description="st_wall_activity;  (stomach wall)")
    st_cnts_activity: float = Field(default=38000.0, ge=0.0, alias="st_cnts_activity", description="st_cnts_activity;   (stomach contents)")
    sm_intest_activity: float = Field(default=16000.0, ge=0.0, alias="sm_intest_activity", description="small_intest_activity;")
    asc_li_activity: float = Field(default=16000.0, ge=0.0, alias="asc_li_activity", description="ascending_large_intest_activity;")
    trans_li_activity: float = Field(default=16000.0, ge=0.0, alias="trans_li_activity", description="transcending_large_intest_activity;")
    desc_li_activity: float = Field(default=16000.0, ge=0.0, alias="desc_li_activity", description="desc_large_intest_activity;")
    rectum_activity: float = Field(default=2500.0, ge=0.0, alias="rectum_activity", description="rectum_activity;")
    intest_air_activity: float = Field(default=11000.0, ge=0.0, alias="intest_air_activity", description="activity of intestine contents (air);")

    ### Abdominal organs ###
    liver_activity: float = Field(default=15000.0, ge=0.0, alias="liver_activity", description="liver_activity;")
    gall_bladder_activity: float = Field(default=42000.0, ge=0.0, alias="gall_bladder_activity", description="gall_bladder_activity;")
    pancreas_activity: float = Field(default=30000.0, ge=0.0, alias="pancreas_activity", description="pancreas_activity;")
    spleen_activity: float = Field(default=13000.0, ge=0.0, alias="spleen_activity", description="spleen_activity;")
    adrenal_activity: float = Field(default=30000.0, ge=0.0, alias="adrenal_activity", description="adrenal_activity;")

    ### Urinary tract ###
    r_kidney_cortex_activity: float = Field(default=29000.0, ge=0.0, alias="r_kidney_cortex_activity", description="right_kidney_cortex_activity;")
    r_kidney_medulla_activity: float = Field(default=35000.0, ge=0.0, alias="r_kidney_medulla_activity", description="right_kidney_medulla_activity;")
    l_kidney_cortex_activity: float = Field(default=28000.0, ge=0.0, alias="l_kidney_cortex_activity", description="left_kidney_cortex_activity;")
    l_kidney_medulla_activity: float = Field(default=35000.0, ge=0.0, alias="l_kidney_medulla_activity", description="left_kidney_medulla_activity;")
    r_renal_pelvis_activity: float = Field(default=37000.0, ge=0.0, alias="r_renal_pelvis_activity", description="right_renal_pelvis_activity;")
    l_renal_pelvis_activity: float = Field(default=37000.0, ge=0.0, alias="l_renal_pelvis_activity", description="left_renal_pelvis_activity;")
    ureter_activity: float = Field(default=4000.0, ge=0.0, alias="ureter_activity", description="ureter activity;")
    urethra_activity: float = Field(default=3000.0, ge=0.0, alias="urethra_activity", description="urethra activity;")
    bladder_activity: float = Field(default=42000.0, ge=0.0, alias="bladder_activity", description="bladder_activity;")

    ### Skeleton ###
    rib_activity: float = Field(default=2400.0, ge=0.0, alias="rib_activity", description="rib_activity;")
    cortical_bone_activity: float = Field(default=15000.0, ge=0.0, alias="cortical_bone_activity", description="cortical_bone_activity;")
    spine_activity: float = Field(default=23000.0, ge=0.0, alias="spine_activity", description="spine_activity;")
    spinal_cord_activity: float = Field(default=20000.0, ge=0.0, alias="spinal_cord_activity", description="spinal_cord_activity;")
    bone_marrow_activity: float = Field(default=16000.0, ge=0.0, alias="bone_marrow_activity", description="bone_marrow_activity;")
    yellow_bone_marrow_activity: float = Field(default=0.0, ge=0.0, alias="yellow_bone_marrow_activity", description="activity value for the yellow marrow")

    ### Vasculature and lymph ###
    art_activity: float = Field(default=11000.0, ge=0.0, alias="art_activity", description="artery_activity;")
    vein_activity: float = Field(default=24000.0, ge=0.0, alias="vein_activity", description="vein_activity;")
    lymph_activity: float = Field(default=2.0, ge=0.0, alias="lymph_activity", description="lymph normal activity;")
    lymph_abnormal_activity: float = Field(default=2.0, ge=0.0, alias="lymph_abnormal_activity", description="lymph abnormal activity;")

    ### Male reproductive ###
    prostate_activity: float = Field(default=30.0, ge=0.0, alias="prostate_activity", description="prostate_activity;")
    sem_activity: float = Field(default=2.0, ge=0.0, alias="sem_activity", description="sem_vess_activity;")
    vas_def_activity: float = Field(default=2.0, ge=0.0, alias="vas_def_activity", description="vas_def_activity;")
    test_activity: float = Field(default=2.0, ge=0.0, alias="test_activity", description="testicular_activity;")
    penis_activity: float = Field(default=2.0, ge=0.0, alias="penis_activity", description="penis_activity")
    epididymus_activity: float = Field(default=2.0, ge=0.0, alias="epididymus_activity", description="epididymus_activity;")
    ejac_duct_activity: float = Field(default=2.0, ge=0.0, alias="ejac_duct_activity", description="ejaculatory_duct_activity;")

    ### Female reproductive ###
    uterus_activity: float = Field(default=60.0, ge=0.0, alias="uterus_activity", description="uterus_activity;")
    vagina_activity: float = Field(default=50.0, ge=0.0, alias="vagina_activity", description="vagina_activity;")
    right_ovary_activity: float = Field(default=40.0, ge=0.0, alias="right_ovary_activity", description="right_ovary_activity;")
    left_ovary_activity: float = Field(default=30.0, ge=0.0, alias="left_ovary_activity", description="left_ovary_activity;")
    fallopian_tubes_activity: float = Field(default=20.0, ge=0.0, alias="fallopian_tubes_activity", description="fallopian tubes_activity;")

    ### Glands, head and neck ###
    parathyroid_activity: float = Field(default=2.0, ge=0.0, alias="parathyroid_activity", description="parathyroid_activity;")
    thyroid_activity: float = Field(default=2.0, ge=0.0, alias="thyroid_activity", description="thyroid_activity;")
    thymus_activity: float = Field(default=60.0, ge=0.0, alias="thymus_activity", description="thymus_activity;")
    salivary_activity: float = Field(default=2.0, ge=0.0, alias="salivary_activity", description="salivary_activity;")
    pituitary_activity: float = Field(default=2.0, ge=0.0, alias="pituitary_activity", description="pituitary_activity;")
    eye_activity: float = Field(default=2.0, ge=0.0, alias="eye_activity", description="eye_activity;")
    lens_activity: float = Field(default=2.0, ge=0.0, alias="lens_activity", description="eye_lens_activity;")

    ### Lesion ###
    lesn_activity: float = Field(default=80.0, ge=0.0, alias="lesn_activity", description="activity for heart lesion, plaque, or spherical lesion")

    ### Brain ###
    brain_activity: float = Field(default=2.0, ge=0.0, alias="brain_activity", description="brain activity;")
    Corpus_Callosum_act: float = Field(default=8.0, ge=0.0, alias="Corpus_Callosum_act", description="activity of Corpus_Callosum")
    Caudate_act: float = Field(default=16.0, ge=0.0, alias="Caudate_act", description="activity of Caudate")
    Internal_capsule_act: float = Field(default=8.0, ge=0.0, alias="Internal_capsule_act", description="activity of Internal_capsule")
    Putamen_act: float = Field(default=16.0, ge=0.0, alias="Putamen_act", description="activity of Putamen")
    Globus_pallidus_act: float = Field(default=16.0, ge=0.0, alias="Globus_pallidus_act", description="activity of Globus_pallidus")
    Thalamus_act: float = Field(default=8.0, ge=0.0, alias="Thalamus_act", description="activity of Thalamus")
    Fornix_act: float = Field(default=8.0, ge=0.0, alias="Fornix_act", description="activity of Fornix")
    Anterior_commissure_act: float = Field(default=8.0, ge=0.0, alias="Anterior_commissure_act", description="activity of Anterior_commissure")
    Amygdala_act: float = Field(default=16.0, ge=0.0, alias="Amygdala_act", description="activity of Amygdala")
    Hippocampus_act: float = Field(default=16.0, ge=0.0, alias="Hippocampus_act", description="activity of Hippocampus")
    Lateral_ventricle_act: float = Field(default=8.0, ge=0.0, alias="Lateral_ventricle_act", description="activity of Lateral_ventricle")
    Third_ventricle_act: float = Field(default=8.0, ge=0.0, alias="Third_ventricle_act", description="activity of Third_ventricle")
    Fourth_ventricle_act: float = Field(default=8.0, ge=0.0, alias="Fourth_ventricle_act", description="activity of Fourth_ventricle")
    Cerebral_aqueduct_act: float = Field(default=8.0, ge=0.0, alias="Cerebral_aqueduct_act", description="activity of Cerebral_aqueduct")
    Mamillary_bodies_act: float = Field(default=8.0, ge=0.0, alias="Mamillary_bodies_act", description="activity of Mamillary_bodies")
    Cerebral_peduncles_act: float = Field(default=8.0, ge=0.0, alias="Cerebral_peduncles_act", description="activity of Cerebral_peduncles")
    Superior_colliculus_act: float = Field(default=8.0, ge=0.0, alias="Superior_colliculus_act", description="activity of Superior_colliculus")
    Inferior_colliculus_act: float = Field(default=8.0, ge=0.0, alias="Inferior_colliculus_act", description="activity of Inferior_colliculus")
    Pineal_gland_act: float = Field(default=8.0, ge=0.0, alias="Pineal_gland_act", description="activity of Pineal_gland")
    Periacquaductal_grey_outer_act: float = Field(default=16.0, ge=0.0, alias="Periacquaductal_grey_outer_act", description="activity of Periacquaductal_grey_outer")
    Periacquaductal_grey_act: float = Field(default=16.0, ge=0.0, alias="Periacquaductal_grey_act", description="activity of Periacquaductal_grey_inner")
    Pons_act: float = Field(default=8.0, ge=0.0, alias="Pons_act", description="activity of Pons")
    Superior_cerebellar_peduncle_act: float = Field(default=8.0, ge=0.0, alias="Superior_cerebellar_peduncle_act", description="activity of Superior_cerebellar_peduncle")
    Middle_cerebellar_peduncle_act: float = Field(default=8.0, ge=0.0, alias="Middle_cerebellar_peduncle_act", description="activity of Middle_cerebellar_peduncle")
    Substantia_nigra_act: float = Field(default=16.0, ge=0.0, alias="Substantia_nigra_act", description="activity of Substantia_nigra")
    Medulla_act: float = Field(default=8.0, ge=0.0, alias="Medulla_act", description="activity of Medulla")
    Medullary_pyramids_act: float = Field(default=8.0, ge=0.0, alias="Medullary_pyramids_act", description="activity of Medullary_pyramids")
    Inferior_olive_act: float = Field(default=8.0, ge=0.0, alias="Inferior_olive_act", description="activity of Inferior_olive")
    Tegmentum_of_midbrain_act: float = Field(default=8.0, ge=0.0, alias="Tegmentum_of_midbrain_act", description="activity of Tegmentum_of_midbrain")
    Midbrain_act: float = Field(default=8.0, ge=0.0, alias="Midbrain_act", description="activity of Midbrain")
    cerebellum_act: float = Field(default=8.0, ge=0.0, alias="cerebellum_act", description="activity of cerebellum")
    white_matter_act: float = Field(default=8.0, ge=0.0, alias="white_matter_act", description="activity of remaining white matter")
    grey_matter_act: float = Field(default=16.0, ge=0.0, alias="grey_matter_act", description="activity of remaining grey matter")
