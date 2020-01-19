from collections import OrderedDict

################################
# Replace '-' with '_'
# Replace ' ' with '_'
# Replace 'ValveBiped_' with ''
# Replace 'Bip01_' with 'Bip'
# Replace 'Bip001_' with 'Bip'
#
# Replace Bone Patterns:
#   Left/Right = \L
#   L/R = \L
################################

bone_list = OrderedDict()
bone_list['hip'] = [
    'Hip',
    'Hips',
    'LowerBody',
    'Lower_Body',
    'Mixamorig:Hips',
    'Pelvis',
    'B_C_Pelvis',
    'Bip_Pelvis',
    'Root',
    'Hips_Root',
    'Rot_Root',
    'Sk',
    'C_Waist_1',
    'Pelwas_001',
    'Waist',
    'HipN',
    'Unused_Root_Hips',
    'Waist01',
    'Waist02',
    'Hips_Root_1',
    'Hips_Root_2',
    'Pelvis_Def',
    'J_Kosi',
    'Kosi',
    'HipMaster_01',
    'J_Bip_C_Hips',
    'J_Hip',
    'Pelvis_L',
    'Pelvis_R',
    'Root_Pelvis_1',
    'Root_X',
]
bone_list['spine'] = [  # This is a list of all spine and chest bones
    'Spine',  # First entry!

    # MMD
    'UpperBody',
    'Upper_Body',
    'Upper_Waist',
    'UpperBody2',
    'Upper_Body_2',
    'Upper_Waist_2',
    'Waist_Upper_2',
    'UpperBody3',
    'Upper_Body_3',
    'Upper_Waist_3',
    'Waist_Upper_3',

    # Mixamo
    'Mixamorig:Spine',
    'Mixamorig:Spine0',
    'Mixamorig:Spine1',
    'Mixamorig:Spine2',
    'Mixamorig:Spine3',
    'Mixamorig:Spine4',

    # 3DMax?
    'Bip_Spine',
    'Bip_Spine0',
    'Bip_Spine1',
    'Bip_Spine2',
    'Bip_Spine3',
    'Bip_Spine4',
    'Bip_Spine5',
    'Bip_Spine00',
    'Bip_Spine01',
    'Bip_Spine02',
    'Bip_Spine03',
    'Bip_Spine04',
    'Bip_Spine05',
    'Bip_Spine_0',
    'Bip_Spine_1',
    'Bip_Spine_2',
    'Bip_Spine_3',
    'Bip_Spine_4',
    'Bip_Spine_5',
    'Bip_Chest',

    # Something
    'B_C_Spine',
    'B_C_Spine0',
    'B_C_Spine1',
    'B_C_Spine2',
    'B_C_Spine3',
    'B_C_Spine4',
    'B_C_Spine5',
    'B_C_Chest',

    # .Mesh
    'Spine_Lower',
    'Spine_Lower_1',
    'Spine_Lower_2',
    'Spine_Middle',
    'Spine_Upper',
    'Spine_Upper_1',
    'Spine_Upper_2',

    'Abdomen',

    'Spine0',
    'Spine1',
    'Spine2',
    'Spine3',
    'Spine4',
    'Spine5',

    'Spine_0',
    'Spine_1',
    'Spine_2',
    'Spine_3',
    'Spine_4',
    'Spine_5',

    'Spine01',
    'Spine02',
    'Spine03',
    'Spine04',
    'Spine05',

    'Spine_01',
    'Spine_02',
    'Spine_03',
    'Spine_04',
    'Spine_05',

    'Spine_A',
    'Spine_B',
    'Spine_C',
    'Spine_D',
    'Spine_E',

    'Spina00',
    'Spina01',
    'Spina02',

    'J_Spine1',
    'J_Spine2',
    'J_Spine3',

    'Spine_Jnt_01',
    'Spine_Jnt_02',
    'Spine_Jnt_03',

    'Chest1',
    'Chest2',
    'Chest3',

    'Chest_A',
    'Chest_B',
    'Chest_C',
    'Chest_D',
    'Chest_E',

    'C_Spine_A_1',
    'C_Spine_B_1',

    'J_Bip_C_Spine',
    'J_Bip_C_Chest',
    'J_Bip_C_UpperChest',

    'Pelwas',
    'Pelwas2',
    'Ribs',

    'BODY1',
    'BODY2',

    'WaistN',
    'BustN',

    'Middle',
    'Bust',

    'SpA',
    'SpB',
    'SpC',

    'Stomach_Def',
    'Chest_Def',

    'TorsoA_01',
    'TorsoB_01',
    'TorsoC_01',

    'Torso_1',
    'Torso_2',

    'AbdomenUpper',
    'ChestLower',

    'Spine_01_X',
    'Spine_02_X',

    'J_Sebo_A',
    'J_Sebo_B',
    'J_Sebo_C',

    'Mune',

    'SpineTop',

    'UpperBodyx2',

    'Chest',

    'Upper_Chest'  # Last entry!
]
bone_list['neck'] = [
    'Neck',
    'Mixamorig:Neck',
    'Head_Neck_Lower',
    'Head_Neck_Lower_1',
    'Head_Neck_Lower_2',
    'Head_Neck_Middle',
    'Bip_Neck',
    'Bip_Neck1',
    'B_C_Neck1',
    'Head_Neck',
    'J_Bip_C_Neck',
    'C_Neck_1',
    'NeckN',
    'Helmet_Lower',
    'Neck_Dev',
    'Neck00',
    'Kubi',
    'J_Kubi',
    'NeckA_01',
    'J_Neck1',
    'NeckLower',
    'Neck_X',
]
bone_list['head'] = [
    'Head',
    'Mixamorig:Head',
    'Head_Neck_Upper',
    'Head_Neck_Upper_1',
    'Head_Neck_Upper_2',
    'Bip_Head',
    'Bip_Head1',
    'B_C_Head',
    'J_Bip_C_Head',
    'C_Head_1',
    'HeadN',
    'Helmet_Upper',
    'Head_01',
    'Head_001',
    'J_Head',
    'Head_X',
    'J_Kao',
]
bone_list['leftShoulder'] = [
    '\L_Shoulder',
    'Shoulder_\L',
    '\LShoulder',
    '\LShoulderN',
    'Shoulder\L',
    'Mixamorig:\LShoulder',
    'Arm_\L_Shoulder',
    'Arm_\L_Shoulder_1',
    'ShoulderArm_\L',
    'Bip_\L_Clavicle',
    'Bip_Collar_\L',
    'B_\L_Shoulder',
    '\LCollar',
    '\L_Clavicle',
    '\L_Clavicle1',
    '\L_Collar',
    '\L_Clavicle_1',
    '\L_CBONE',
    'Shoulder+_\L',
    'Shol_\L',
    '\Lf_Clavicle',
    'Clavicle_\L',
    'Arm_\L_Sh_1',
    'Shoulder(\L)_0',
    '\L_Kata',
    'Cf_D_Shoulder_\L',
    'Cf_D_Shoulder2_\L',
    'Clavicle\LT_01',
    'J_Bip_\L_Shoulder',
    'J_\L_Collar',
    'J_\L_Shoulder',
    'Clavicle\L',
    'Bip_Clavicle_\L',
    '\L_Clavic',
    'J_Sako_\L',
    '\L_ShoulderPad',
    'Collarbone_\L',
]
bone_list['leftUpperArm'] = [
    '\L_Arm',
    '\LArm',
    'Arm_\L',
    '\LArmA',
    'ArmTC_\L',
    '+_\L_Elbow_Support',
    'Mixamorig:\LArm',
    'Arm_\L_Shoulder_2',
    'Bip_\L_UpperArm',
    'Bip_UpperArm_\L',
    'B_\L_Arm1',
    'Upper_Arm_\L',
    'UpperArm_\L',
    '\L_Upper_Arm',
    '\LShldr',
    '\L_UpperArm',
    '\LUpArm',
    'Uparm_\L',
    '\L_Uparm',
    '\L_Arm_01',
    'Arm_\L_Arm',
    '\L_Upperarm_1',
    'ArmFor_Correction_\L',
    '\L_ARM1',
    'Arm\L1',
    '\LShoulderJ',
    '\Lf_Shoulder',
    'Arm_Upper_\L',
    'Arm_\L_Sh_2',
    '\Larm1',
    'Shoulder(\L)_1',
    '\L_Ude',
    'Shoulder\LT_01',
    'J_Bip_\L_UpperArm',
    'J_\L_UpArm',
    'J_\L_Elbow',
    'Arm_1_\L',
    'Upperarm01_\L',
    '\L_Shldr',
    '\LShldrBend',
    'Arm_Stretch_\L',
    'J_Ude_A_\L'
]
bone_list['leftLowerArm'] = [
    '\L_Elbow',
    '\LElbow',
    'Elbow_\L',
    'Mixamorig:\LForeArm',
    'Arm_\L_Elbow',
    'Bip_\L_ForeArm',
    'Bip_LowerArm_\L',
    'B_\L_Arm2',
    'Fore_Arm_\L',
    'ForeArm_\L',
    '\LForeArm',
    '\L_ForeArm',
    '\LLowArm',
    '\L_Foarm',
    'Loarm_\L',
    '\L_Arm_02',
    '\L_Forearm_1',
    'Lower_Arm_\L',
    'ElbowFor_Correction_\L',
    '\L_ARM2',
    'Arm\L2',
    '\LArmJ',
    'Elb_\L',
    'Arm_\L_Elbow_1',
    'LowerArm_\L',
    '\Lf_Elbow',
    'Arm_Lower_\L',
    '\L_Forarm',
    '\Larm2',
    'Hand(\L)07',
    'Lowarm_\L',
    '\L_Hiji',
    'Elbow\LT_01',
    'J_Bip_\L_LowerArm',
    'J_\L_ForeArm',
    'Arm_2_\L',
    'Bip_Forearm_\L',
    'Lowerarm01_\L',
    '\LForearmBend',
    'Forearm_Stretch_\L',
    'J_Ude_B_\L',
]
bone_list['leftHand'] = [
    '\L_Wrist',
    '\LWrist',
    'Wrist_\L',
    'Wrist2_\L',
    'HandAux2_\L',
    'Mixamorig:\LHand',
    'Arm_\L_Wrist',
    'Arm_\L_Wirst',
    'Bip_\L_Hand',
    'Bip_Hand_\L',
    'B_\L_Hand',
    'Hand_\L',
    'Hand\L',
    '\LHand',
    '\LHandN',
    '\L_Hand',
    '\L_Hand_1',
    '\LFingerBaseN',
    '\Lf_Wrist',
    'Palm_\L',
    'Hand(\L)00',
    '\L_Te',
    'Hand\LT_01',
    'J_Bip_\L_Hand',
    'J_\L_Wrist',
    'J_Te_\L'
]
bone_list['leftUpLeg'] = [
    '\L_Leg',
    '\L_Foot',
    '\LLeg',
    'Leg_\L',
    'Leg_\L_001',
    'Leg\L1',
    'LegWAux_\L',
    'Leg00003333_\L',
    'Leg00004444_\L',
    'Mixamorig:\LUpLeg',
    'Leg_\L_Thigh',
    'Bip_\L_Thigh',
    'Bip_Hip_\L',
    'B_\L_Leg1',
    'Upper_Leg_\L',
    '\LThigh',
    'Thigh_\L',
    '\L_Thigh',
    '\LUpLeg',
    '\LHip',
    'Upleg_\L',
    '\L_Hip',
    '\L_Leg_01',
    '\L_Femur',
    'Waist_Cancel_\L',
    'Waist_Cancellation_\L',
    '\L_Femur_1',
    '\L_LEG1',
    '\LLegJ',
    'Tg_\L',
    'Leg_\L_Thigh_1',
    'UpperLeg_\L',
    '\Lf_Leg',
    '\L_UpLeg',
    'Thigh00_\L',
    '\Lfoot1',
    'Leg(\L)04',
    '\L_Momo',
    'Leg_Thigh_\L',
    'Hip\LT_01',
    'J_Bip_\L_UpperLeg',
    'J_\L_UpLeg',
    'Leg\L',
    'Leg_1_\L',
    'Bip_Thigh_\L',
    'Groin_\L',
    'Upperleg01_\L',
    '\LThighBend',
    'Thigh_Stretch_\L',
    'J_Asi_A_\L'
]
bone_list['leftLeg'] = [
    '\L_Knee',
    '\LKnee',
    'Knee_\L_001',
    'Knee_\L',
    'Mixamorig:\LLeg',
    'Leg_\L_Knee',
    'Bip_\L_Calf',
    'Bip_Knee_\L',
    'B_\L_Leg2',
    'Lower_Leg_\L',
    '\LLeg',
    '\LShin',
    'Shin_\L',
    '\L_Calf',
    'Calf_\L',
    '\LLowLeg',
    '\L_Shin',
    'Loleg_\L',
    '\L_Leg_02',
    '\L_KneeLower',
    'Tibia_\L',
    '\L_Tibia',
    '\L_Tibia_1',
    '\L_LEG2',
    'Leg\L2',
    '\LKneeJ',
    'LowerLeg_\L',
    '\Lf_Knee',
    'Leg01_\L',
    '\Lfoot2',
    'Leg(\L)00',
    '\L_Sune',
    'Leg_Calf_\L',
    'Knee\LT_01',
    'J_Bip_\L_LowerLeg',
    'J_\L_Leg',
    'Knee\L',
    'Leg_2_\L',
    'Bip_Leg_\L',
    'Lowerleg01_\L',
    'Leg_Stretch_\L',
    'J_Asi_B_\L',
]
bone_list['leftFoot'] = [
    '\L_Ankle',
    '\L_Ankle_001',
    'Ankle_\L',
    'Mixamorig:\LFoot',
    'Leg_\L_Ankle',
    'Eg_\L_Ankle',
    'Bip_\L_Foot',
    'Bip_Foot_\L',
    'B_\L_Foot',
    'Lower',
    '\LFoot',
    'Foot_\L',
    'Foot\L',
    '\L_Foot',
    'Leg_\L_Foot',
    '\L_Foot_01',
    'LegIK_\L',
    '\L_Foot_1',
    '\L_FOOT1',
    '\LFootJ',
    '\Lf_Ankle',
    '\L_Heel',
    'Leg(\L)02',
    '\L_Asi',
    'Foot\LT_01',
    'J_Bip_\L_Foot',
    'J_\L_Foot',
    '\LAnkle',
    'J_Asi_D_\L',
]
bone_list['leftToe'] = [
    '\L_Toe',
    '\L_Toes',
    '\LToe',
    '\LToe1',
    'LegTip_\L',
    'LegTipEX_\L',
    'ClawTipEX_\L',
    'Mixamorig:\LToeBase',
    'Leg_\L_Toes',
    'Bip_\L_Toe0',
    'B_\L_Toe',
    'Toe_\L',
    'Toe\L',
    '\L_Toe1',
    '\L_Toe2',
    '\LToeBase',
    'Toe1_1_\L',
    'Leg_\L_Foot_Toes',
    'ToeSaki_\L',
    '\L_Toe0',
    '\L_Toe_1',
    '\L_FOOT2',
    '\LToeN',
    '\LToeA',
    'Toes_\L',
    'ToeTip_\L',
    'ToeTip2_\L',
    '\Lf_Toe',
    'Tsumasaki_\L',
    'Leg_\L_Toe',
    'Leg(\L)03',
    'Toe\LT_01',
    'J_Bip_\L_ToeBase',
    'J_\L_Toe',
    'Bip_Toe_\L',
    'Toe_Boot_\L',
    'Toes_01_\L',
    'J_Asi_E_\L',
]