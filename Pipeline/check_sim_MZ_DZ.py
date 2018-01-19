#! /usr/bin/env python
# coding=utf-8

# Check for similarity between MZ and DZ
import pandas as pd
from os.path import join as pjoin
import nibabel as nib
from ATT.algorithm import tools
import numpy as np

tableparpath = '/nfs/s2/userhome/huangtaicheng/hworkingshop/hcp_test/tables'
MZ_lbl = pd.read_csv(pjoin(tableparpath, 'MZ_lbl.csv'))
DZ_lbl = pd.read_csv(pjoin(tableparpath, 'DZ_lbl.csv'))


MZ_nsubj = len(MZ_lbl)
DZ_nsubj = len(DZ_lbl)

data_parpath = '/nfs/s2/userhome/huangtaicheng/hworkingshop/hcp_test'
task = 'EMOTION'
smooth = '4'

MZ_r = []
MZ_p = []
# MZ similarity
for n in range(MZ_nsubj):
    twin1ID_MZ = MZ_lbl['Twin1'][n]
    twin2ID_MZ = MZ_lbl['Twin2'][n]
    twin1data_MZ = nib.load(pjoin(data_parpath, twin1ID_MZ, 'MNINonLinear', 'Results', 'tfMRI_'+task, 'tfMRI_'+task+'_hp200_s'+smooth+'_level2.feat', twin1ID_MZ+'_tfMRI_'+task+'_level2_hp200_s'+smooth+'.dscalar.nii')).get_data()
    twin2data_MZ = nib.load(pjoin(data_parpath, twin2ID_MZ, 'MNINonLinear', 'Results', 'tfMRI_'+task, 'tfMRI_'+task+'_hp200_s'+smooth+'_level2.feat', twin2ID_MZ+'_tfMRI_'+task+'_level2_hp200_s'+smooth+'.dscalar.nii')).get_data()
    r_tmp_MZ, p_tmp_MZ = tools.pearsonr(twin1data_MZ, twin2data_MZ)
    MZ_r.append(r_tmp_MZ)
    MZ_p.append(p_tmp_MZ)
MZ_r = np.array(MZ_r)
MZ_p = np.array(MZ_p)

DZ_r = []
DZ_p = []
# DZ similarity
for n in range(MZ_nsubj):
    twin1ID_DZ = DZ_lbl['Twin1'][n]
    twin2ID_DZ = DZ_lbl['Twin2'][n]
    twin1data_DZ = nib.load(pjoin(data_parpath, twin1ID_DZ, 'MNINonLinear', 'Results', 'tfMRI_'+task, 'tfMRI_'+task+'_hp200_s'+smooth+'_level2.feat', twin1ID_DZ+'_tfMRI_'+task+'_level2_hp200_s'+smooth+'.dscalar.nii')).get_data()
    twin2data_DZ = nib.load(pjoin(data_parpath, twin2ID_DZ, 'MNINonLinear', 'Results', 'tfMRI_'+task, 'tfMRI_'+task+'_hp200_s'+smooth+'_level2.feat', twin2ID_DZ+'_tfMRI_'+task+'_level2_hp200_s'+smooth+'.dscalar.nii')).get_data()
    r_tmp_DZ, p_tmp_DZ = tools.pearsonr(twin1data_DZ, twin2data_DZ)
    DZ_r.append(r_tmp_DZ)
    DZ_p.append(p_tmp_DZ)
DZ_r = np.array(DZ_r)
DZ_p = np.array(DZ_p)
 





