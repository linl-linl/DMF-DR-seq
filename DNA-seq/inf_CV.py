# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 20:32:21 2020

@author: cyclopenta
"""


import os
from collections import defaultdict
info_dict = defaultdict(list)
os.system('ls *CV.txt > info_cv_temp')
col_list = ['AVG', 'STD', 'CV', 'Total Count', 'file_name']
with open('info_cv_temp', 'r') as REF:
    for line in REF:
        line = line.rstrip()
        with open(line, 'r')as file:
            for i in file:
                i = i.rstrip()
                inf = i.split(':')[1]
                info_dict[line].append(inf)
info_dict = dict(info_dict)
with open('CV_result_table.txt', 'w') as OUT:
    line_str = ''
    for col in col_list:
        line_str += col
        line_str += '\t'
    line_str += '\n'
    OUT.write(line_str)
    for fn,content in info_dict.items():
        line_str = ''
        for i in content:
            line_str += i 
            line_str += '\t'
        line_str += fn
        line_str += '\t'
        line_str += '\n'
        OUT.write(line_str)
os.system('rm info_cv_temp')
print('done')
        
                
                
                
