# !usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
from collections import defaultdict

file_anno = open('cell_dna.txt', 'r')
dict_anno = defaultdict(list)
for i in file_anno:
    i = i.rstrip().split('\t')
    dict_anno[i[1]].append(i[0])
dict_anno = dict(dict_anno)
file_anno.close()

df = pd.read_csv('SegCopy_1M', sep='\t')
for group, sample_list in dict_anno.items():
    df2 = df[['CHR', 'START', 'END']+sample_list]
    df2.to_csv(group+'_SegCopy', sep='\t', index=False)

