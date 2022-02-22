# ！usr/bin/env python
# -*- coding:utf-8 -*-

# python Gfilter_3cor_none.py expr1.txt expr2.txt expr3.txt filter_threshold/0/1/none

import sys
from decimal import Decimal

expr1 = sys.argv[1]
file1 = open(expr1, 'r')
cont1 = file1.readlines()
dict1 = {}
header1 = cont1[0].rstrip()
for m in cont1[1:]:
    m = m[:-1]
    m = m.split('\t')
    g = m[0]
    e = m[1]
    dict1[g] = e
file1.close()

expr2 = sys.argv[2]
file2 = open(expr2, 'r')
cont2 = file2.readlines()
dict2 = {}
header2 = cont2[0].rstrip()
for n in cont2[1:]:
    n = n[:-1]
    n = n.split('\t')
    g = n[0]
    e = n[1]
    dict2[g] = e
file2.close()

expr3 = sys.argv[3]
file3 = open(expr3, 'r')
cont3 = file3.readlines()
dict3 = {}
header3 = cont3[0].rstrip()
for n in cont3[1:]:
    n = n[:-1]
    n = n.split('\t')
    g = n[0]
    e = n[1]
    dict3[g] = e
file3.close()

listg = []
t_str = sys.argv[4]
if (t_str == 'none'):
    listg = dict1.keys()
else:
    t = float(t_str)
    for k, v in dict1.items():
        if (t == 0):
            if Decimal(v) == 0 and Decimal(dict2[k]) == 0 and Decimal(dict3[k]) == 0:
                continue
            else:
                listg.append(k)
        else:
            if Decimal(v) < t and Decimal(dict2[k]) < t and Decimal(dict3[k]) < t:
                continue
            else:
                listg.append(k)

cell = expr1.split('_')[0]
fileout = open(cell+'_3filter'+t_str+'.txt', 'w')
fileout.write('\t'+header1+'\t'+header2+'\t'+header3+'\n')
for i in listg:
    fileout.write(i+'\t'+dict1[i]+'\t'+dict2[i]+'\t'+dict3[i]+'\n')
fileout.close()

