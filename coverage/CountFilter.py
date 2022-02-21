#!/usr/bin/env python
#coding=utf-8

import re
import codecs
import argparse

parser = argparse.ArgumentParser(description='top/middle/bottom1000 gene-counts: \
                                              python2 CountFilter.py -f GeneReadCount.txt')

parser.add_argument('-f', '--gcount', type=str, required=True, help='GeneReadCount.txt')

args = parser.parse_args()


file_count=open(args.gcount,'r')
prefix=re.sub('_GeneReadCount.txt','',args.gcount)
dict_count={}
for line in file_count:
    if ('Read Count' in line) or ('Gene Count' in line):
        continue
    else:
        line2=re.sub('\n','',line)
        l=line2.split('\t')
        dict_count[line2]=int(l[1])
dict_order=sorted(dict_count.items(),key=lambda x:x[1],reverse=True)
dict_order2=sorted(dict_count.items(),key=lambda x:x[1],reverse=False)

file_order=codecs.open(prefix+'_counts_order.txt','w')
for i in dict_order:
    file_order.write(i[0]+'\n')

file_top=codecs.open(prefix+'_counts_top1000.txt','w')
count=0
for i in dict_order:
    file_top.write(i[0]+'\n')
    count=count+1
    if (count >= 1000):
        break

file_middle=codecs.open(prefix+'_counts_middle1000.txt','w')
length=int(len(dict_order))
if (length%2 == 0):
    m=length/2
    s=m-499
    e=m+500
    c=0
    for i in dict_order:
        c=c+1
        if (c < s):
            continue
        elif (s <= c <= e):
            file_middle.write(i[0]+'\n')
        else:
            break
else:
    m=(length+1)/2
    s=m-500
    e=m+499
    c=0
    for i in dict_order:
        c=c+1  
        if (c < s):
            continue   
        elif (s <= c <= e):
            file_middle.write(i[0]+'\n')
        else:
            break

file_bottom=codecs.open(prefix+'_counts_bottom1000.txt','w')
count=0
for i in dict_order2:
    file_bottom.write(i[0]+'\n')
    count=count+1
    if (count >= 1000):
        break

file_count.close()
file_order.close()
file_top.close()
file_middle.close()
file_bottom.close()








