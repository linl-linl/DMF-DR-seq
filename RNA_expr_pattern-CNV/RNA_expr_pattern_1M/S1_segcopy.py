# !usr/bin/env python
# -*- coding:utf-8 -*-

# python segcopy.py infercnv.observations.txt

import sys
import re
import os
import numpy as np

url = '/home/songjia/newdisk/xuxing_multiomics/RNA/expr_pattern2/test_3same_ref/script/'
#file = open(url+'seg_gene_info.txt', 'r')
file = open(url+'seg_gene_info_1M.txt', 'r')
info = file.readlines()
file.close()

infercnv = sys.argv[1]
os.system('''cp %s %sgenecopy_infercnv.txt''' % (infercnv, url))
os.system('''sed -i 's/"//g' %sgenecopy_infercnv.txt''' % (url))
file_gc = open(url+'genecopy_infercnv.txt', 'r')
GC = file_gc.readlines()
gc = []
for i in GC:
    i = re.sub('"', '', i)
    i = re.sub(' ', '\t', i)
    gc.append(i)
dict_gc = {}
for i in gc:
    gene = i.split('\t')[0]
    copy = i.rstrip().split('\t')[1:]
    dict_gc[gene] = copy
sample_num = len(copy)
file_gc.close()
os.system('''rm %sgenecopy_infercnv.txt''' % (url))

# segcopy
url2 = re.sub('infercnv.observations.txt', '', sys.argv[1])
out = open(url2+'segcopy', 'w')
out2 = open(url2+'segcopy2', 'w')
header = 'CHR\tSTART\tEND\t'+gc[0]
out.write(header)
out2.write(gc[0])
for i in info[1:]:
    chrn = i.split('\t')[0].split(':')[0]
    b_start = i.split('\t')[1].split(':')[0]
    b_end = i.split('\t')[1].split(':')[1]
    b_len = i.split('\t')[1].split(':')[2]
    b_copy = []
    if (len(i.split('\t')) < 3):
        b_copy = ['NA' for n in range(sample_num)]
    elif i.split('\t')[2] == '':
        b_copy = ['NA' for n in range(sample_num)]
    else:
        list_g = i.split('\t')[2].split(';')
        g_num = 0
        for g in list_g:
            gene = g.split(':')[0]
            glen_on_bin = g.split(':')[4]
            if gene in dict_gc:
                # g_copy = list(float(x)*int(glen_on_bin) for x in dict_gc[gene])
                g_num = g_num+1
                g_copy = list(float(x) for x in dict_gc[gene])
                if b_copy == []:
                    b_copy = g_copy
                else:
                    b_copy = list(np.sum([b_copy, g_copy], axis=0))
        if b_copy == []:
            b_copy = ['NA' for n in range(sample_num)]
            #b_copy = ['0' for n in range(sample_num)]
        else:
            # b_copy = list(float(x)/int(b_len) for x in b_copy)
            b_copy = list(float(x)/int(g_num) for x in b_copy)
            b_copy = list(str(x) for x in b_copy)
    line = '\t'.join(b_copy)+'\n'
    out.write(chrn+'\t'+b_start+'\t'+b_end+'\t'+line)
    out2.write(line)
out.close()
out2.close()

