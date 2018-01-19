#!/usr/bin/env python
# coding=utf-8

from twinstudy.PrepData import extcsv
import numpy as np

datapath = '../../../tables/RESTRICTED_liqinqin_5_22_2017_22_29_56.csv'

clscsv = extcsv.OperateCSV(datapath)
subjid = clscsv.rawdata['Subject']

MZsubjid = clscsv.find_values_by_key('Subject', 'ZygosityGT', 'MZ').tolist()
DZsubjid = clscsv.find_values_by_key('Subject', 'ZygosityGT', 'DZ').tolist()

Nontwinid_temp = [sid for sid in subjid if sid not in MZsubjid]
Nontwinid = [sid for sid in Nontwinid_temp if sid not in DZsubjid]

MZ_data = clscsv.get_data_by_row('Subject', MZsubjid)
DZ_data = clscsv.get_data_by_row('Subject', DZsubjid)

MZ_familyid = clscsv.unique_value_by_key('Family_ID', data=MZ_data)
DZ_familyid = clscsv.unique_value_by_key('Family_ID', data=DZ_data)


MZ_lbl = [clscsv.find_values_by_key('Subject', 'Family_ID', mzsid, data=MZ_data).tolist() for mzsid in MZ_familyid]
DZ_lbl = [clscsv.find_values_by_key('Subject', 'Family_ID', dzsid, data=DZ_data).tolist() for dzsid in DZ_familyid]

MZ_familyid = np.expand_dims(np.array(MZ_familyid),axis=-1)
DZ_familyid = np.expand_dims(np.array(DZ_familyid),axis=-1)
MZ_lbl = np.array(MZ_lbl)
DZ_lbl = np.array(DZ_lbl)

MZ_savedata = np.concatenate((MZ_familyid.T, MZ_lbl.T)).T
DZ_savedata = np.concatenate((DZ_familyid.T, DZ_lbl.T)).T
