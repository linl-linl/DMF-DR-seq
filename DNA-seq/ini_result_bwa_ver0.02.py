# -*- coding: utf-8 -*-
"""
Created on Thu May 13 20:53:05 2021

@author: cyclopenta
"""


import os
import pandas as pd
from collections import Counter
file_name = 'map_summay'
interest_info = Counter()
os.system(' ls *_map > bwacsv_file_temp.txt')
interest_ini = ['total qc-passed reads', 'total qc-failed reads', 'reads mapped %','reads properly paired %']
temp_file = open ('bwacsv_file_temp.txt')
for ini in interest_ini:
    interest_info[ini] ={}
row_list= []
for f in temp_file:
    f = f.rstrip()
    row_list.append(f)
    fh = open(f)
    temp= []
    for line in fh:
        line = line.rstrip()
        temp.append(line)
    interest_info['total qc-passed reads'][f] =temp[0].split()[0]
    interest_info['total qc-failed reads'][f] = temp[0].split()[2]
    interest_info['reads mapped %'][f] = temp[4].split('(')[1].split(':')[0].rstrip()
    interest_info['reads properly paired %'][f] = temp[8].split('(')[1].split(':')[0].rstrip()

df_list = []
for row in row_list:
    temp_dic = {key:val[row] for key,val in interest_info.items()}
    temp_dic['filename'] = row
    temp_dic = pd.DataFrame([temp_dic])
    df_list.append(temp_dic)
final_df = pd.concat(df_list)
os.system('''rm bwacsv_file_temp.txt''' )
final_df.to_csv(file_name +'.csv', index=False)