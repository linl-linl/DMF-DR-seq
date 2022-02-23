# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 15:54:54 2021

@author: cyclopenta
"""


import argparse
import os
parser = argparse.ArgumentParser(description='''plot CIRCOS, note that the script runs under R 3.6 \
                                 and make sure mycircos_final.R under the directory''')
parser.add_argument('--input', required=True, type=str, help='specify the input file list')
parser.add_argument('--suffix', required=True, type=str, help='specify suffix of gene-related files\
                    for example, use _filtered_filtered.txt when you filter the genelist twice')
params = parser.parse_args()
file_list = params.input
suff = params.suffix
with open(file_list, 'r')as process:
    for line in process:
        # 一定要有这行不然R会报错 因为\n的自动换行
        line = line.rstrip()
        CNV_file = line
        prefix = CNV_file.split('cnv.txt')[0]
        gene_amp = prefix + 'ampGenelist' + suff
        gene_del = prefix + 'delGenelist' + suff
        out = prefix + '_circosplot.pdf'
        os.system('''Rscript mycircos_final.R {0} {1} {2} {3}'''.format(CNV_file, gene_amp, gene_del, out))
print('DONE')
