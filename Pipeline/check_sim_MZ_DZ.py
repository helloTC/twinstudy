#! /usr/bin/env python
# coding=utf-8

# Check for similarity between MZ and DZ
import pandas as pd
from os.path import join as pjoin
import nibabel as nib
from ATT.algorithm import tools
import numpy as np
from ATT.iofunc import iofiles

tableparpath = '/nfs/s2/userhome/huangtaicheng/hworkingshop/hcp_test/tables'
data_parpath = '/nfs/s2/userhome/huangtaicheng/hworkingshop/hcp_test'
outpath = '/nfs/s2/userhome/huangtaicheng/hworkingshop/hcp_test/output'

MZ_lbl = pd.read_csv(pjoin(tableparpath, 'MZ_lbl.csv'))
DZ_lbl = pd.read_csv(pjoin(tableparpath, 'DZ_lbl.csv'))

MZ_nsubj = len(MZ_lbl)
DZ_nsubj = len(DZ_lbl)

task = 'EMOTION'
smooth = '4'

MZ_r = []
MZ_p = []

dropgrp_MZ = []
dropgrp_DZ = []
# MZ similarity
for n in range(MZ_nsubj):
    twin1ID_MZ = str(MZ_lbl['Twin1'][n])
    twin2ID_MZ = str(MZ_lbl['Twin2'][n])
    try:
        twin1data_MZ = nib.load(pjoin(data_parpath, twin1ID_MZ, 'MNINonLinear', 'Results', 'tfMRI_'+task, 'tfMRI_'+task+'_hp200_s'+smooth+'_level2.feat', twin1ID_MZ+'_tfMRI_'+task+'_level2_hp200_s'+smooth+'.dscalar.nii')).get_data()
        twin2data_MZ = nib.load(pjoin(data_parpath, twin2ID_MZ, 'MNINonLinear', 'Results', 'tfMRI_'+task, 'tfMRI_'+task+'_hp200_s'+smooth+'_level2.feat', twin2ID_MZ+'_tfMRI_'+task+'_level2_hp200_s'+smooth+'.dscalar.nii')).get_data()
    except IOError as e:
        dropgrp_MZ.append(n)
        continue
    r_tmp_MZ, p_tmp_MZ = tools.pearsonr(twin1data_MZ, twin2data_MZ)
    MZ_r.append(r_tmp_MZ)
    MZ_p.append(p_tmp_MZ)
MZ_r = np.array(MZ_r)
MZ_p = np.array(MZ_p)

DZ_r = []
DZ_p = []

# DZ similarity
for n in range(DZ_nsubj):
    twin1ID_DZ = str(DZ_lbl['Twin1'][n])
    twin2ID_DZ = str(DZ_lbl['Twin2'][n])
    try:
        twin1data_DZ = nib.load(pjoin(data_parpath, twin1ID_DZ, 'MNINonLinear', 'Results', 'tfMRI_'+task, 'tfMRI_'+task+'_hp200_s'+smooth+'_level2.feat', twin1ID_DZ+'_tfMRI_'+task+'_level2_hp200_s'+smooth+'.dscalar.nii')).get_data()
        twin2data_DZ = nib.load(pjoin(data_parpath, twin2ID_DZ, 'MNINonLinear', 'Results', 'tfMRI_'+task, 'tfMRI_'+task+'_hp200_s'+smooth+'_level2.feat', twin2ID_DZ+'_tfMRI_'+task+'_level2_hp200_s'+smooth+'.dscalar.nii')).get_data()
    except IOError as e:
        dropgrp_DZ.append(n)
        continue
    r_tmp_DZ, p_tmp_DZ = tools.pearsonr(twin1data_DZ, twin2data_DZ)
    DZ_r.append(r_tmp_DZ)
    DZ_p.append(p_tmp_DZ)
DZ_r = np.array(DZ_r)
DZ_p = np.array(DZ_p)

MZ_lbl = MZ_lbl.drop(dropgrp_MZ)
DZ_lbl = DZ_lbl.drop(dropgrp_DZ) 

outpkl = {}
outpkl['DZ_r'] = DZ_r
outpkl['DZ_p'] = DZ_p
outpkl['MZ_r'] = MZ_r
outpkl['MZ_p'] = MZ_p
outpkl['MZ_lbl'] = MZ_lbl
outpkl['DZ_lbl'] = DZ_lbl

iopkl = iofiles.make_ioinstance(pjoin(outpath, 'global_sim_'+ task +'_s'+smooth+'.pkl'))
iopkl.save(outpkl)





