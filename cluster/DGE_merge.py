#!/usr/bin/env python
#coding=utf-8

import re
import numpy as np
import time
import argparse

def boolean_string(s):
    if s not in {'False', 'True'}:
        raise ValueError('Not a valid boolean string')
    return s == 'True'

parser = argparse.ArgumentParser(description='合并DGE文件: python DGE_merge.py \
                                                           -d1 dge1 -d2 dge2 \
                                                           -s1 sample_name1 -s2 sample_name2 \
                                                           -t1 True/False -t2 True/False')

parser.add_argument('-d1', '--dge1', type=str, required=True, help='dge file 1')
parser.add_argument('-d2', '--dge2', type=str, required=True, help='dge file 2')
parser.add_argument('-s1', '--sample1', type=str, default='', help='sample name 1. It is required when -t1 True')
parser.add_argument('-s2', '--sample2', type=str, default='', help='sample name 2. It is required when -t2 True')
parser.add_argument('-t1', '--tag1', default=False, type=boolean_string, help='Bool type: True/False. tag cell barcode with sample name')
parser.add_argument('-t2', '--tag2', default=False, type=boolean_string, help='Bool type: True/False. tag cell barcode with sample name')

args = parser.parse_args()


## 运行时间
begin_time = time.time()

## 读入矩阵
file_dge1=open(args.dge1,'r')
file_dge2=open(args.dge2,'r')
cont_dge1=file_dge1.readlines()
cont_dge2=file_dge2.readlines()
sample_name1=args.sample1
sample_name2=args.sample2

## 合并2个矩阵的cell barcode
## if判断是否要对cell barcode加sample tag
cell_dge1=cont_dge1[0]
cell_dge1=re.sub('\n','',cell_dge1)
cell_dge1=cell_dge1.split('\t')[1:]
if args.tag1 :
    cell_dge1_tag=[]
    for i in cell_dge1:
        newi=sample_name1+'_'+i
        cell_dge1_tag.append(newi)
else:
    cell_dge1_tag=cell_dge1
cell_dge2=cont_dge2[0]
cell_dge2=re.sub('\n','',cell_dge2)
cell_dge2=cell_dge2.split('\t')[1:]
if args.tag2 :
    cell_dge2_tag=[]
    for i in cell_dge2:
        newi=sample_name2+'_'+i
        cell_dge2_tag.append(newi)
else:
    cell_dge2_tag=cell_dge2
cell_num_dge1=len(cell_dge1_tag)
cell_num_dge2=len(cell_dge2_tag)
cell_merge=['GENE']+cell_dge1_tag+cell_dge2_tag
print(cell_merge)

## 合并2个矩阵的gene name
info_dge1=cont_dge1[1:]
info_dge2=cont_dge2[1:]
gene_dge1=[]
gene_dge2=[]
for i in info_dge1:
    g=re.match(r'(.*?)\t', i)
    gene=g.group(1)
    gene_dge1.append(gene)
for i in info_dge2:
    g=re.match(r'(.*?)\t', i)
    gene=g.group(1)
    gene_dge2.append(gene)
gene_merge = gene_dge1+gene_dge2
gene_merge = set(gene_merge)

## 以dict1/2分别储存表达矩阵
## k = gene name
## v = expression
dict_dge1={}
dict_dge2={}
for i in info_dge1:
    i2=re.sub('\n','',i)
    i3=i2.split('\t')
    i4=i3[0]
    i5=i3[1:]
    dict_dge1[i4]=i5
for i in info_dge2:
    i2=re.sub('\n','',i)
    i3=i2.split('\t')
    i4=i3[0]
    i5=i3[1:]
    dict_dge2[i4]=i5

## 合并表达矩阵
## for循环整合表达情况：对于仅在某个表达矩阵中出现的gene name，在另一个矩阵中的表达量设为0
list_merge=[]
list_merge.append(cell_merge)
for i in gene_merge:
    if (i in dict_dge1) and (i in dict_dge2):
        line=[i]+dict_dge1[i]+dict_dge2[i]
    elif (i in dict_dge1) and (i not in dict_dge2):
        fill2=['0' for index in range(cell_num_dge2)]
        line=[i]+dict_dge1[i]+fill2
    elif (i not in dict_dge1) and (i in dict_dge2):
        fill1=['0' for index in range(cell_num_dge1)]
        line=[i]+fill1+dict_dge2[i]
    list_merge.append(line)
file_merge=open('DGE_merge.txt','w')
for l in list_merge:
    m=''
    for n in l :
        m=m+n+'\t'
    m=m[:-1]
    file_merge.write(m+'\n')
file_merge.close()

## 运行时间
end_time = time.time()
run_time = float(end_time-begin_time)/60
print(run_time)
