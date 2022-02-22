# ！usr/bin/env python
# -*- coding:utf-8 -*-

# count转化为fpkm
# CountToFPKM.R is required!!!

import os
import re
import argparse

parser = argparse.ArgumentParser(description='将目录下的(或指定的)count.txt转化为fpkm.txt \
                                              python cluster_count_fpkm.py \
                                              -c list_count')

parser.add_argument('-c', '--count', type=str, default=0, help='a list of count.txt')

args = parser.parse_args()


# save count_url to list_count
if args.count:
    list_count = []
    file_count = open(args.count, 'r')
    for i in file_count:
        count_name=re.sub('\n', '', i)
        list_count.append(count_name)
else:
    os.system("ls *count.txt > list_count")
    list_count = []
    file_count = open('list_count', 'r')
    for i in file_count:
        count_url = re.sub('\n', '', i)
        list_count.append(count_url)
    os.system("rm list_count")

# CountToFpkm
list_FPKM = []
list_fpkm = []
for count in list_count:
    prefix = re.sub('_count.txt', '', count)
    FPKM = prefix+'_FPKM.txt'
    fpkm = prefix+'_fpkm.txt'
    list_FPKM.append(FPKM)
    list_fpkm.append(fpkm)
    
    filein = count
    fileout = FPKM
    os.system("Rscript CountToFPKM.R %s %s" % (filein, fileout))
    
    file_FPKM = open(FPKM, 'r')
    file_fpkm = open(fpkm, 'w')
    cont_FPKM = file_FPKM.readlines()
    cont_fpkm = []
    for line in cont_FPKM:
        line = re.sub('"', '', line)
        cont_fpkm.append(line)
    file_fpkm.write('GENE\t'+prefix+'\n')
    for line in cont_fpkm:
        file_fpkm.write(line)
    file_FPKM.close()
    file_fpkm.close()

