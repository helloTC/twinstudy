#!/usr/bin/env python
# coding=utf-8

import nibabel as nib
from os.path import join as pjoin
from ATT.algorithm import tools
from ATT.util import plotfig
import numpy as np

subjid = '100307'
parpath = pjoin('/home/hellotc/', subjid, 'MNINonLinear/Results/')
task_name = 'WM'
smooth = '12'
data = nib.load(pjoin(parpath, 'tfMRI_'+task_name, 'tfMRI_'+task_name+'_hp200_s'+smooth+'_level2.feat', subjid+'_tfMRI_'+task_name+'_level2_hp200_s'+smooth+'.dscalar.nii')).get_data()

with open(pjoin(parpath, 'tfMRI_'+task_name, 'tfMRI_'+task_name+'_hp200_s'+smooth+'_level2.feat', 'Contrasts.txt'), 'r') as f:
    contrasts = f.read().splitlines()

r, p = tools.pearsonr(data, data)

plotmat = plotfig.make_figfunction('mat')
plotmat(r, np.arange(1, len(contrasts)+1), np.arange(1, len(contrasts)+1))
