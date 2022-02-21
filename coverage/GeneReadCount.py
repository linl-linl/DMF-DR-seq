#!/usr/bin/env python
#coding=utf-8

import re
import codecs
import argparse

parser = argparse.ArgumentParser(description='取同一深度，计算所测到的基因数——统计counts.txt文件中测到的基因和对应的read数，末尾显示测到的基因数: \
                                              python2 GeneReadCount.py \
                                              -f counts.txt')

parser.add_argument('-f', '--txtfile', type=str, required=True, help='$label\_counts.txt')

args = parser.parse_args()

file = open(args.txtfile,'r')
prefix = re.sub('_counts.txt','',args.txtfile)
file_count = codecs.open(prefix+'_GeneReadCount.txt','w')
count=0
for line in file:
    if ('processed' in line) or ('__' in line):
        continue
    else:
        line2 = re.sub('\n','',line)
        l = line2.split('\t')
        if (l[1] != '0'):
            count=count+1
            file_count.write(l[0]+'\t'+l[1]+'\n')
file_count.write('Gene Count: '+str(count))
file.close()
file_count.close()


        
