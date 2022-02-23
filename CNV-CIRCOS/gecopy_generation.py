# -*- coding: utf-8 -*-
"""
Created on Mon May 17 15:18:14 2021

@author: cyclopenta
"""


import os
import pandas as pd

os.system('ls *rmdupdelGenelist_filtered_filtered.txt > genecopy_temp')
out_list = []
with open('genecopy_temp', 'r') as myfiles:
    for line in myfiles:
        line = line.rstrip()
        file1 = line
        pre = line.split('delGenelist_filtered_filtered.txt')[0]
        file2 = pre + 'ampGenelist_filtered_filtered.txt'
        out_list.append(pre +'Genecopy.txt')
        with open(pre +'Genecopy.txt','w')as OUT:
            with open(file1, 'r') as f1:
                f1.readline()
                OUT.write('CHR\tSTART\tEND\tSTRAND\tGene.refGene\tFunc.refGene\t' + pre + '\n')
                for i in f1:
                    OUT.write(i)
            with open(file2, 'r')as f2:
                f2.readline()
                for i in f2:
                    OUT.write(i)
os.system('rm genecopy_temp')

drop_list = ['CHR', 'START', 'END','Func.refGene','STRAND']
origin = pd.read_csv(out_list[0], sep ='\t')
origin = origin.drop(drop_list, axis = 1)
total = len(out_list) - 1
count = 1
for f in out_list[1:]:
    tmp = pd.read_csv(f, sep = '\t')
    tmp = tmp.drop(drop_list, axis = 1)
    origin = pd.merge(origin, tmp, on=['Gene.refGene'], how = 'outer')
    print('{:.2f}% completed'.format(count/total*100))
    count += 1
origin = origin.fillna(2)
origin_dup = origin[origin['Gene.refGene'].duplicated()]
mytmp = origin_dup.groupby(['Gene.refGene']).agg('mean')
mytmp.reset_index(inplace = True)
dup_list = list(set(list(origin_dup['Gene.refGene'])))
# 去重去的干净
for i in dup_list:
    origin = origin[origin['Gene.refGene'] != i]
origin = pd.concat([origin,mytmp])
origin.to_csv('all_gecopy.txt', header = True, index = False, sep = '\t')

