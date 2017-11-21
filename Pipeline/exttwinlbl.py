#!/usr/bin/env python
# coding=utf-8

from twinstudy.PrepData import extcsv

datapath = '/home/hellotc/workingshop/workwares/data/behdata/hcp/RESTRICTED_liqinqin_5_22_2017_22_29_56.csv'

clscsv = extcsv.OperateCSV(datapath)

MZsubjid = clscsv.find_values_by_key('Subject', 'ZygosityGT', 'MZ').tolist()
DZsubjid = clscsv.find_values_by_key('Subject', 'ZygosityGT', 'DZ').tolist()

MZ_data = clscsv.get_data_by_row('Subject', MZsubjid)
DZ_data = clscsv.get_data_by_row('Subject', DZsubjid)

MZ_familyid = clscsv.unique_value_by_key('Family_ID', data=MZ_data)
DZ_familyid = clscsv.unique_value_by_key('Family_ID', data=DZ_data)

MZ_lbl = [clscsv.find_values_by_key('Subject', 'Family_ID', mzsid, data=MZ_data).tolist() for mzsid in MZ_familyid]
DZ_lbl = [clscsv.find_values_by_key('Subject', 'Family_ID', dzsid, data=DZ_data).tolist() for dzsid in DZ_familyid]


