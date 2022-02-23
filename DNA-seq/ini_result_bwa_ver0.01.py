# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 15:40:02 2020

@author: cyclopenta
"""


import pandas as pd
import sys
import os
import re
from collections import Counter

'''
15034243 + 0 in total (QC-passed reads + QC-failed reads)
371029 + 0 secondary
0 + 0 supplementary
0 + 0 duplicates
14944208 + 0 mapped (99.40% : N/A)
14663214 + 0 paired in sequencing
7331607 + 0 read1
7331607 + 0 read2
13950576 + 0 properly paired (95.14% : N/A)
14536480 + 0 with itself and mate mapped
36699 + 0 singletons (0.25% : N/A)
200948 + 0 with mate mapped to a different chr
150540 + 0 with mate mapped to a different chr (mapQ>=5)

'''
interest_info = Counter()
os.system(' ls *_map > bwacsv_file_temp.txt')
interest_ini = ['total qc-passed reads', 'total qc-failed reads', 'reads mapped %','reads properly paired %', 'singLetons %']
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
    interest_info['singLetons %'][f] = temp[10].split('(')[1].split(':')[0].rstrip()

df_list = []
for row in row_list:
    temp_dic = {key:val[row] for key,val in interest_info.items()}
    temp_dic['filename'] = row
    temp_dic = pd.DataFrame([temp_dic])
    df_list.append(temp_dic)
    
final_df = pd.concat(df_list)
os.system('''rm bwacsv_file_temp.txt''' )

output_name = input('Enter the output name:\n')

final_df.to_csv(output_name+'.csv', index=False)

    
        
        

