from pyxcat.parameter_sets.activity import ActivityParameters
from pyxcat.parameter_sets.attenuation import AttenuationParameters
from pyxcat.parameter_sets.body import BodyParameters
from pyxcat.parameter_sets.cardiac import CardiacParameters
from pyxcat.parameter_sets.image import ImageParameters
from pyxcat.parameter_sets.lesion import LesionParameters
from pyxcat.parameter_sets.respiration import RespirationParameters

parameter_notes ="""
#--------------------------------------------------------------------------
#                             NOTES:
#--------------------------------------------------------------------------
#NOTE 0: The phantom program can be run in different modes as follows.  
#  Mode 0: standard phantom generation mode that will generate phantoms of the
#          body.
#  Mode 1: lesion generator that will create phantoms of only the user
#          defined lesion which can be in the heart or kidneys. Subtract these phantoms from those 
#          of mode 0 to place the defect in the body.
#  Mode 2: spherical lesion generator that will create phantoms of only the
#          user defined lesion. Add these phantoms to those of mode 0 to place
#          the lesions in the body.
#  Mode 3: cardiac plaque generator that will create phantoms of only the
#          user defined plaque. Add these phantoms to those of mode 0 to place
#          the plaques in the body.
#  Mode 4: vector generator that will output motion vectors as determined from 
#          the phantom surfaces. The vectors will be output as text files.
#  Mode 5: anatomy generator will save the phantom produced from the user-defined anatomy 
#          parameters. The phantom is saved as two files, the organ file and the heart_base 
#          file. The names of these files can then be specified in the parfile for later runs
#          with the program not having to take the time to generate the anatomy again. In using 
#	   	   a saved anatomy, be sure to set all scalings back to 1; otherwise, the anatomy will be 
#          scaled again.       
#
#NOTE 1: The average phantom is the average ONLY OF THOSE FRAMES GENERATED. That is,
#  if you specify that only 2 frames be generated, then the average phantom is
#  just the average of those 2 frames.
#  ***************************************************************************
#  ** FOR A GOOD AVERAGE, generate at least 8-16 frames per 1 complete heart
#  ** cycle and/or per 1 complete respiratory cycle.
#  ***************************************************************************
#
#NOTE 2: Heart motion refers to heart BEATING or contraction, while resp.
#  motion refers to organ motion due to breathing. Note that the entire heart is
#  translated or rotated due to resp. motion, even if it is not contracting.
#  ** IF motion_option=1 , THE HEART WILL MOVE (TRANSLATE) BUT NOT BEAT.****
#
#NOTE 3:   Users sets the length and starting phase of both the heart
#          and respiratory cycles. NORMAL values for length of heart beat and
#          respiratory are cycles are 1 sec. and 5 secs., respectively,
#          BUT THESE CAN VARY AMONG PATIENTS.
#
#          An index value between 0 and 1 is used the specify the starting phase
#          of the heart or resp cycles. IF NO MOTION IS SPECIFIED THEN THE STARTING
#          PHASE IS USED AS THE SINGLE PHASE AT WHICH THE PHANTOM IS GENERATED.
#          (see documentation for more details).
#
#NOTE 3A:  These parameters control the LV volume curve of the heart. The user can specify the LV
#	  	   volume at 5 points in the cardiac cycle. Check the logfile to see what the default volumes 
#          are. The end-diastolic volume can only be reduced. The way to increase it would be to change
#          the overall heart scale. The end-systolic volume can be increased or reduced. The other volumes
#          need to have values between the end-diastolic and end-systolic volumes.  The time durations for the
#          different portions of the cardiac cycle must add up to a total of 1.
#
#          Changing these parameters will alter the heart_curve. The altered curve and heart files can be output using
#          mode = 5.
#
#NOTE 4:  These NORMAL values are for normal tidal breathing.
#  ** Modeling a deep inhale may require higher values. **
#
#  The AP_expansion parameter controls the anteroposterior diameter of the ribcage, body,
#  and lungs. The ribs rotate upward to expand the chest cavity by the amount indicated by the 
#  AP_expansion parameter. The lungs and body move with the expanding ribs. There is maximum amount
#  by which the AP diameter can expand, due to the size of the ribs (some expansions are impossible
#  geometrically.) If the user specifies too great an expansion, the program will terminate with an
#  error message. 
#
#  The diaphragm motion controls the motion of the liver, the left diaphragm, stomach, spleen and
#  all organs downstream from them. 
#
#  The heart has its own parameters to control its motion. It can translate left or right (+/- values of hrt_motion_x respectively), 
#  to the anterior/posterior (+/- values of hrt_motion_y respectively), or up/down (+/- values of hrt_motion_z respectively) 
#  with the diaphragm motion. The heart can also rotate. The x-axis runs from the right side of the body to the left.  
#  Changing the x-rot will tilt the heart up(+ values)/down (- values). The y-axis runs from the front of the body to the back.  
#  Changing the y-rot will tilt the heart from side to side. The z-axis runs from the feet to the head.  
#  The z-rot will spin the heart right or left.
#
#NOTE 5:  The phantom program outputs statistics on these anatomical parameters in the logfile it generates. The logfile is 
#         named with the extension *_log. These statistics can be used to determine the amount of scaling desired. Be aware 
#	  	  the phantom scaling parameters scale the entire phantom; therefore, any body, heart or breast scalings will
#         be additional to this base scaling.
#
#NOTE 6:   Location of air in the large intestine and rectum
#          5 = air visible in the entire large intestine and rectum
#          4 = air visible in ascending, transverse, descending, and sigmoid portions of the large intestine 
#          3 = air visible in ascending, transverse, and descending portions of the large intestine
#          2 = air visible in ascending and transverse portions of the large intestine
#          1 = air visible in ascending portion of the large intestine only
#          0 = no air visible (entire large intestine and rectum filled with contents)
#          
#
#NOTE 7:
#        - The phantom dimensions do not necessarily have to be cubic. The array_size parameter 
#          determines the x and y dimensions of the images. The number of slices in the z dimension 
#          is determined by the start_slice and end_slice parameters. The total number of slices is
#          end_slice - start_slice + 1.
#
#NOTE 8:
#        - rotation parameters determine
#          initial orientation of beating (dynamic) heart LV long axis
#        - d_zy_rotation : +y-axis rotates toward +z-axis (about x-axis) by beta
#          d_xz_rotation : +z-axis rotates toward +x-axis (about y-axis) by phi
#          d_yx_rotation : +x-axis rotates toward +y-axis (about z-axis) by psi
#
#        - Based on patient data, the mean and SD heart orientations are:
#                zy_rot = -110 degrees (no patient data for this rotation)
#                xz_rot = 23 +- 10 deg.
#                yx_rot = -52 +- 11 deg.
#
#	 - Phantom will output total angles for the heart orientation in the logfile
#
#NOTE 9: Creates lesion (defect) for the LEFT VENTRICLE of the heart or the LEFT or RIGHT KIDNEYS ONLY.
#
#  lesion_type: specifies the organ in which to place the lesion (0 = heart, 1 = right kidney, 2 - left kidney)
#
#--------------------------------
#  theta_center: location of lesion center in circumferential dimension
#
#  For the LV of the heart, these angles correspond to:
#  theta center =    0.0  => anterior wall
#  theta center =  +90.0  => lateral   "
#  theta center = +180.0  => inferior  "
#  theta center = +270.0  => septal    "
#
#  For the KIDNEYS, these correspond to:
#  theta center =    0.0  => left lateral wall
#  theta center =  +90.0  => posterior   "
#  theta center = +180.0  => right lateral  "
#  theta center = +270.0  => anterior    "
#--------------------------------
#  theta_width : lesion width in circumferential dimension
#
#  TOTAL width of defect in degrees. So for example a width of 90 deg.
#  means that the width is 45 deg. on either side of theta center.
#--------------------------------
#  x center :   lesion center in long-axis dimension (heart) or z-axis (kidneys)
#
#  x center = 0    -> base of LV  -> top of kidney
#  x center = 1.0  -> apex of LV  -> bottom of kidney
#--------------------------------
#  x width:  lesion width in long-axis dimension (heart) or z-axis (kidneys)
#
#  total width. Defect extend half the total width on either side of the
#  x_center.
#
#  NOTE: if the specified width extends beyond the boundaries of the organ
#        then the defect is cut off and the effective width is less than the
#        specified width. So for example...
#
#--------------------------------
#  Wall_fract : fraction of the organ wall that the lesion transgresses
#  Wall_fract = 0.0 => transgresses none of the wall
#  Wall_fract = 0.5 => transgresses the inner half of the wall
#  Wall_fract = 1.0 => trangresses the entire wall
#--------------------------------
#
#
#NOTE 10: Creates a spherical lesion in the XCAT phantom. Depending on where the lesion is placed, it will move with
#         the respiratory motion. Location of the lesion is specified in pixel values. Initial location of the lesion
#         needs to be with respect to end-expiration. 
#
#
#NOTE 11: Creates a plaque in the coronary vessel tree that will move with the cardiac/respiratory motion
#
#---------------------------------------------------------------------------
#  plaque_center: location of plaque along the length of the specified artery
#    center = 0    -> base of artery
#    center = 1.0  -> apex of artery
#
#-------------------------------------------
#  plaque_thickness : plaque thickness in mm.
#
#-------------------------------------------
#  plaque_width :   plaque width in mm.
#
#-------------------------------------------
#  plaque_length :  plaque length in mm.
#
#------------------------------------------------------
#  plaque_id  :  vessel to place the plaque in
#
#        aorta 
#        rca1
#        rca2
#        lad1
#        lad2
#        lad3
#        lcx
#------------------------------------------------------
#
#
#NOTE 12: Using mode = 4, vectors are output for each voxel of frame 1 to the current frame. The vectors show the motion
#         from the 1st frame to frame N. The vectors are output as text files with the format of 
#         output_name_vec_frame1_frameN.txt.  NOTE that the program only outputs the non-zero vectors so vectors may not be output for every voxel.
#
#         The output vectors are a combination of known sampled points from the phantom objects and vectors interpolated
#         from these sampled points.  The known vectors are designated as such in the vector output.  You can increase
#         the number of known points (and accuracy of the vector output) by increasing the parameter vec_factor.
#
#
#NOTE 13: See instructions "Creating_user_objects_for_XCAT". If including user objects, be sure to set the use_activ_material_table to 1 and setup the 
#	  activ_material_table_file to include definitions for the acitivities and materials of the new objects
"""