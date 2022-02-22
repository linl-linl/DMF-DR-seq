# !/usr/bin/env python
# -*- coding:utf-8 -*-

# python exon_length_gtf_fadj.py
# 调整exon_length_gtf.txt的格式

import re

file_e = open('cluster_exon_length_gtf.txt', 'r')
file_o = open('cluster_exon_length_gtf_fadj.txt', 'w')
file_o.write('GENE\tLENGTH\n')
cont_e = file_e.readlines()
for i in cont_e:
    i = re.sub('\n', '', i)
    i = i.split('\t')
    if (len(i)==2):
        g = re.sub('\"', '', i[0])
        lh = i[1]
        file_o.write(g+'\t'+lh+'\n')
    else:
        continue
file_e.close()
file_o.close()
