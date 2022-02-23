# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:10:03 2021

@author: cyclopenta
"""


import sys

file = sys.argv[1]
out = sys.argv[2]
with open(file, 'r')as gtf:
    with open(out, 'w')as OUT:
        OUT.write('CHR\tSTART\tEND\tSTRAND\tGene.refGene\n')
        for line in gtf:
            if line.startswith('#'):
                continue
            else:
                info = line.split('\t')
                if info[2] == 'gene' or info[2] == 'pseudogene':
                    ge_name = line.split('gene_name')[1].split(';')[0].lstrip(' "').rstrip('"')
                    OUT.write(info[0] + '\t' + info[3] + '\t' + info[4] + '\t' + info[6] + '\t' + ge_name + '\n')
print('Done')

