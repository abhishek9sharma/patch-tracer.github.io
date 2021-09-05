#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
-----------------------------------------
@Created: 2020/11/01
------------------------------------------
@Modify: 2020/11/01
------------------------------------------
@Description:

"""
import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
sys.path.append('../')
sys.path.append('../..')
sys.path.append('../../..')

from vulnerability_analysis.utility import json_processing, log, file_processing

list_file_content = file_processing.read_TXTfile('list')
CVE_NOTES_data = {}
CVEID = ''
NOTE = ''
for ele_line in list_file_content.split('\n'):
    if ele_line.startswith('CVE-'):
        CVEID = ele_line.split(' ')[0].strip('\n')
    elif ele_line.startswith('	NOTE: '):
        NOTE_contens = ele_line.split(' ')
        for NOTE in NOTE_contens:
            if 'http' in NOTE:
                if CVEID in CVE_NOTES_data.keys():
                    CVE_NOTES_data[CVEID].append(NOTE)
                else:
                    CVE_NOTES_data[CVEID] = [NOTE]
json_processing.write(json_content=CVE_NOTES_data , path='list_tem.json')





