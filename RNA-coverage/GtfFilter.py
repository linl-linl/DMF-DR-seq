#!/usr/bin/env python
#coding=utf-8

import re
import argparse

parser = argparse.ArgumentParser(description='python2 GtfFilter.py \
                                              -f counts_order.txt \
                                              -g gtf file')

parser.add_argument('-f', '--count', type=str, required=True, help='counts_order.txt')
parser.add_argument('-g', '--gtf', type=str, required=True, help='gtf file')

args = parser.parse_args()

file_gene=open(args.count,'r')
list_gene=[]
for l in file_gene:
    l2=re.sub('\n','',l)
    l3=l2.split('\t')
    list_gene.append(l3[0])
file_gene.close()

file_gtf=open(args.gtf,'r')
dict_gtf={}
#pattern=r'gene_name "(.*?)";'
pattern=r'gene_id "(.*?)";'
for l in file_gtf:
    if (l.startswith('#')) or (l == '') or (l == '\n'):
        continue
    else:
        m=re.search(pattern,l)
        dict_gtf[m.group(1)]=0
file_gtf.close()

for i in list_gene:
    dict_gtf[i]=1

file_gtf=open(args.gtf,'r')
prefix=re.sub('.txt','',args.count)
file_out=open(prefix+'_new.gtf','w')
for l in file_gtf:
    if (l.startswith('#')) or (l == '') or (l == '\n'):
        continue
    else:
        m=re.search(pattern,l)
    if dict_gtf[m.group(1)]:
        file_out.write(l)
file_gtf.close()
file_out.close()



