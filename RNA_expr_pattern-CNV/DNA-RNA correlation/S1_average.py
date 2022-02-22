# !usr/bin/env python
# -*- coding:utf-8 -*-

import re
import pandas as pd


def average(filename):
    header = re.sub('_SegCopy', '', filename)
    header = re.sub('_segcopy', '', header)
    df = pd.read_csv(filename, sep='\t')
    df2 = df.drop(['CHR', 'START', 'END'], axis=1)
    df3 = pd.DataFrame(df2.mean(1))
    df3.columns = [header]
    df3.to_csv(header+'_average', sep='\t', index=False)


aa = ['H_Bulk', 'H_F', 'H_W', 'M_Bulk', 'M_F', 'M_W', 'S_Bulk', 'S_F', 'S_W']
for i in aa:
    D = i+'D_SegCopy'
    R = i+'R_segcopy'
    average(D)
    average(R)

