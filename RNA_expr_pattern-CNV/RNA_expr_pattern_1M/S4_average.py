# !usr/bin/env python
# -*- coding:utf-8 -*-

# python average.py

import os
import pandas as pd

H = ['test_H_Bulk', 'test_H_FR2', 'test_H_WR']
M = ['test_M_ERR_Bulk', 'test_M_ERR_FR', 'test_M_ERR_WR']
S = ['test_S_ERR_Bulk', 'test_S_ERR_FR', 'test_S_ERR_WR']
ll = H+M+S

for u in ll:
    segcopy2 = u+'/segcopy2'
    segcopy3 = u+'/segcopy3'
    segcopy4 = u+'/segcopy4'
    segcopy5 = u+'/segcopy5'
    #df = pd.read_csv(segcopy3, sep='\t')
    # allbin
    df = pd.read_csv(segcopy2, sep='\t')
    #n = len(df.columns.values)
    df[['AVERAGE']] = pd.DataFrame(df.mean(1))
    #df.to_csv(segcopy4, sep='\t', index=False)
    # allbin
    df.to_csv(segcopy5, sep='\t', index=True)
    os.system('''Rscript average.R %s''' % (u))
    os.system('''Rscript chr_average.R %s''' % (u))

