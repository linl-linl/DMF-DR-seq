# !usr/bin/env python
# -*- coding:utf-8 -*-

# python average.py

import os
import pandas as pd

H = ['H_BulkD', 'H_FD', 'H_WD']
M = ['M_BulkD', 'M_FD', 'M_WD']
S = ['S_BulkD', 'S_FD', 'S_WD']
ll = H+M+S
ll=S
for u in ll:
    segcopy = u+'_SegCopy'
    segcopy2 = u+'_SegCopy2'
    df = pd.read_csv(segcopy, sep='\t')
    df = df.drop(['CHR', 'START', 'END'], axis=1)
    df[['AVERAGE']] = pd.DataFrame(df.mean(1))
    df.to_csv(segcopy2, sep='\t', index=False)
    os.system('''Rscript S3_DNA3.R %s''' % (u))

