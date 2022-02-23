# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 16:09:59 2021

@author: cyclopenta
"""


import os
import argparse
import pandas as pd
from collections import defaultdict

parser = argparse.ArgumentParser(description='''ANNOVAR CNV annotations and custom large-scale CNV extraction''')
parser.add_argument('--input', required=True, type=str, help='specify the input file')
parser.add_argument('--neutral', required=False, type=int, default=2, help='specify the threshold for CNV identification')
parser.add_argument('--chrlength', required=False, type=str, default='/home/songjia/reference/hg19/STAR/chrNameLength.txt', help='specify \
                    the chrlength file for large-scale CNV identification, contigs will be discarded')
parser.add_argument('--largescale', required=False, type=float, default= 0.33, help='specify \
                    the threshold for large-scale CNV identification, default is 0.33 of every chr')

def annovar_call(path, avin, prefix):
    os.system(''' {0}table_annovar.pl {1} {0}humandb/ -buildver hg19 -out {2} -remove -protocol refGene -operation g'''
              .format(path, avin, prefix))


def gene_list(anno):
    pre = anno.split('.hg19_multianno.txt')[0]
    with open(anno, 'r')as ref:
        ge_dict = defaultdict(list)
        info_dict = defaultdict(list)
        line_count = 0
        with open(pre + '.mergedbins', 'r')as meg:
            for line in meg:
                line_count += 1
                if line_count == 1:
                    continue
                copy = line.split()[-1]
                info_dict[line_count] += copy
        info_dict = dict(info_dict)
        line_count = 0
        for line in ref:
            line_count += 1
            if line_count == 1:
                continue
            ges = line.split()[6].split(';')
            tag = line.split()[5]
            ge_dict[line_count] += ges
            info_dict[line_count].append(tag)
        ge_dict = dict(ge_dict)
        for k, v in ge_dict.items():
            ge_dict[k] = list(set(v))
        with open(pre + 'Genelist.txt', 'w')as OUT:
            OUT.write('Func.refGene' + '\t' + 'Gene.refGene' + '\t' + 'Copynumber' + '\n')
            str_tmp = ''
            for k, v in ge_dict.items():
                for g in v:
                    cn = str(info_dict[k][0])
                    fun = info_dict[k][1]
                    str_tmp += fun + '\t' + g + '\t' + cn + '\n'
            OUT.write(str_tmp)



params = parser.parse_args()
file = params.input
thresh = params.neutral
large_thresh = params.largescale
chr_len_file = params.chrlength
df = pd.read_csv(file, sep = '\t')
skip_box = ['CHR', 'START', 'END']
annovar_path = '/home/songjia/software/annovar/'
chr_len_dict = {}
all_file_list = []
ge_file_list = []
with open(chr_len_file, 'r')as tmp:
    for line in tmp:
        line = line.rstrip()
        info = line.split()
        chrname = info[0]
        chrlen = int(info[1])
        chr_len_dict[chrname] = chrlen
for index, col in df.iteritems():
    if index in skip_box:
        continue
    else:
        col_list = skip_box + [index]
        name_amp = index + 'amp'
        name_del = index + 'del'
        df_tmp = pd.DataFrame(df, columns = col_list)
        df_tmp.to_csv(index + 'cnv.txt', sep = '\t', header = True, index = False)
        # amp file generation and large-scale calling
        df_amp = df_tmp[df_tmp[index] > thresh]
        df_amp = df_amp.reset_index(drop=True)
        last = len(df_amp)
        for i, r in df_amp.iterrows():
            if i < last - 1:
                if df_amp.loc[i, 'END'] + 1 == df_amp.loc[i+1, 'START']:
                    # fen cheng liang hang yin wei bu xiang tai chang 
                    if df_amp.loc[i, 'CHR'] == df_amp.loc[i+1, 'CHR']:
                        if df_amp.loc[i, index] == df_amp.loc[i+1, index]:
                            df_amp.loc[i+1, 'START'] = df_amp.loc[i,'START']
                            df_amp = df_amp.drop(i)
        df_amp.to_csv(name_amp + '.mergedbins',header = True, index = False, sep = '\t')
        df_amp['large-scale'] = 0
        for i, r in df_amp.iterrows():
            if df_amp.loc[i, 'END'] - df_amp.loc[i, 'START'] > chr_len_dict[df_amp.loc[i, 'CHR']] * 0.33:
                df_amp.loc[i, 'large-scale'] = 1
        df_amp_large = df_amp[df_amp['large-scale'] == 1]
        df_amp_large = df_amp_large.drop('large-scale', axis = 1)
        df_amp_large.to_csv(name_amp + '_large.txt', index = False, header = True, sep = '\t')
        df_amp = df_amp.drop([index, 'large-scale'], axis = 1)
        df_amp['ref'] = 0
        df_amp['obs'] = 0
        df_amp.to_csv(name_amp + '.avinput', header = None, index = False, sep = '\t')
        all_file_list.append(name_amp + '.avinput')
        ge_file_list.append(name_amp + '.hg19_multianno.txt')
        # del file generation and large-scale calling
        df_del = df_tmp[df_tmp[index] < thresh]
        df_del = df_del.reset_index(drop=True)
        last = len(df_del)
        for i, r in df_del.iterrows():
            if i < last - 1:
                if df_del.loc[i, 'END'] + 1 == df_del.loc[i+1, 'START']:
                    # fen cheng liang hang yin wei bu xiang tai chang 
                    if df_del.loc[i, 'CHR'] == df_del.loc[i+1, 'CHR']:
                        if df_del.loc[i, index] == df_del.loc[i+1, index]:
                            df_del.loc[i+1, 'START'] = df_del.loc[i,'START']
                            df_del = df_del.drop(i)
        df_del.to_csv(name_del + '.mergedbins',header = True, index = False, sep = '\t')
        df_del['large-scale'] = 0
        for i, r in df_del.iterrows():
            if df_del.loc[i, 'END'] - df_del.loc[i, 'START'] > chr_len_dict[df_del.loc[i, 'CHR']] * 0.33:
                df_del.loc[i, 'large-scale'] = 1
        df_del_large = df_del[df_del['large-scale'] == 1]
        df_del_large = df_del_large.drop('large-scale', axis = 1)
        df_del_large.to_csv(name_del + '_large.txt', index = False, header = True, sep = '\t')
        df_del = df_del.drop([index, 'large-scale'], axis = 1)
        df_del['ref'] = 0
        df_del['obs'] = 0
        df_del.to_csv(name_del + '.avinput', header = None, index = False, sep = '\t')
        all_file_list.append(name_del + '.avinput')
        ge_file_list.append(name_del + '.hg19_multianno.txt')
print('File preparation Done!', flush = True)
for f in all_file_list:
    out_pre = f.split('.avinput')[0]
    annovar_call(annovar_path, f, out_pre)
print('ANNOVAR Done!', flush = True)
for f in ge_file_list:
    gene_list(f)
print('Gene List Generation Done!', flush = True)