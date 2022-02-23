# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 16:04:07 2021

@author: cyclopenta
"""


import pandas as pd
import argparse

parser = argparse.ArgumentParser(description='''Filter CNV genes by given data''')
parser.add_argument('--input', required=True, type=str, help='specify the input file list')
parser.add_argument('--reference', required=False, type=str, default='/home/songjia/reference/cancer/cancerGeneList.tsv', help='specify the reference')
parser.add_argument('--position', required=False, type=str, default='/home/songjia/reference/hg19/hg19_CNV_REF.txt', help='specify the position annotation file')
parser.add_argument('--posflag', required=False, type=int, default=0, help='specify whether need to annotate gene positions, \
                    default is 0, you should only annotate the gene positions during the final filtering step')
def write_file(kong):
    with open (kong, 'w')as OUT:
        OUT.write('Gene.refGene' + '\t' + 'Func.refGene' + '\n')
params = parser.parse_args()
file_list = params.input
reference = params.reference
pos = params.position
flag = params.posflag
name_dict = {'Hugo Symbol': 'Gene.refGene'}
df_ref = pd.read_csv(reference, sep = '\t')
df_pos = pd.read_csv(pos, sep = '\t')
df_gene = pd.DataFrame(df_ref, columns = ['Hugo Symbol'])
df_gene = df_gene.rename(columns = name_dict)
with open(file_list, 'r')as IN:
    for line in IN:
        line = line.rstrip()
        out_pre = line.split('.txt')[0]
        try:
            df_tmp = pd.read_csv(line, sep = '\t')
        except pd.errors.EmptyDataError:
            write_file(out_pre + '_filtered.txt')
        df_merge = pd.merge(df_gene, df_tmp, on ='Gene.refGene')
        if flag:
            df_merge_pos = pd.merge(df_pos, df_merge, on = 'Gene.refGene')
        else:
            df_merge_pos = df_merge
        df_merge_pos.to_csv(out_pre + '_filtered.txt', header = True, index = False, sep = '\t')
print('done')