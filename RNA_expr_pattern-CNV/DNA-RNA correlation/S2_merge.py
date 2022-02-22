# !usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd

aa = ['H_Bulk', 'H_F', 'H_W', 'M_Bulk', 'M_F', 'M_W', 'S_Bulk', 'S_F', 'S_W']
bb = {}
for i in aa:
    D = i+'D_average'
    R = i+'R_average'
    bb[D] = pd.read_csv(D, sep='\t')
    bb[R] = pd.read_csv(R, sep='\t')

flag = 0
for v in bb.values():
    if flag == 0:
        df = v
        flag = 1
    else:
        df = pd.concat([df, v], axis=1)
df = df.dropna()
df.to_csv('Merge', sep='\t', index=False)

