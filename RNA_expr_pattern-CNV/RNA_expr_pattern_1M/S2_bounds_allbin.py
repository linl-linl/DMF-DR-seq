# !usr/bin/env python
# -*- coding:utf-8 -*-

# python bounds.py url

import sys

url = sys.argv[1]
if url[-1] != '/':
    url = url+'/'
segcopy = url+'segcopy'
segcopy2 = url+'segcopy2'
segcopy3 = url+'segcopy3'
bounds = url+'bounds_allbin'

#file = open(segcopy2, 'r')
#cont = file.readlines()
#file.close()

#out = open(segcopy3, 'w')
#out.write(cont[0])
#for i in cont[1:]:
#    if 'NA' in i:
#        continue
#    else:
#        out.write(i)
#out.close()

file = open(segcopy, 'r')
cont = file.readlines()
file.close()

b = open(bounds, 'w')
row_count = 1
chr1 = ''
chr2 = ''
for i in cont[1:]:
    row_count = row_count+1
    chr2 = i.split('\t')[0]
    if chr2 != chr1:
        if chr2 == 'chr1':
            chr1 = chr2
            continue
        else:
            b.write(chr1+'\t'+str(row_count-1)+'\n')
            chr1 = chr2
b.write(chr1+'\t'+str(row_count-1))
b.close()

