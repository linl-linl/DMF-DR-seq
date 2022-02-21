# !usr/bin/env python
# -*- coding:utf-8 -*-

# python DNA_bounds.py

segcopy = 'SegCopy_1M'
bounds = 'DNA_bounds'

file = open(segcopy, 'r')
cont = file.readlines()
file.close()

b = open(bounds, 'w')
row_count = 1
chr1 = ''
chr2 = ''
for i in cont[1:]:
    if 'NA' in i:
        continue
    else:
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

