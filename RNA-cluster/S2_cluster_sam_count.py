# ！usr/bin/env python
# -*- coding:utf-8 -*-

# 用htseq-count，由Aligned.out.sam计算read counts
# 调整read counts文件为count表达

import os
import re
import argparse

parser = argparse.ArgumentParser(description='由目录下的(指定的)Aligned.out.sam提取read counts，生成表达矩阵: \
                                              python cluster_sam_count.py \
                                              -s list_sam \
                                              -g url_gtf')

parser.add_argument('-s', '--sam', type=str, default=0, help='a list of Aligned.out.sam')
parser.add_argument('-g', '--gtf', type=str, default='/home/songjia/reference/hg19/gencode.v35lift37.annotation.gtf', help='gtf file for htseq-count')

args = parser.parse_args()


# save sam_url to list_sam
if args.sam:
    list_sam=[]
    file=open(args.sam,'r')
    for i in file:
        sam_name=re.sub('\n','',i)
        list_sam.append(sam_name)
else:
    os.system("ls *Aligned.out.sam > list_Aligned.out.sam")
    list_sam = []
    file_sam = open('list_Aligned.out.sam', 'r')
    for i in file_sam:
        sam_url = re.sub('\n', '', i)
        list_sam.append(sam_url)
    os.system("rm list_Aligned.out.sam")

# htseq-count: output "gene\tcount"
gtf = args.gtf
list_counts = []
for sam in list_sam:
    prefix = re.sub('Aligned.out.sam', '', sam)
    htseq_out = prefix+'_counts.txt'
    list_counts.append(htseq_out)
    os.system("htseq-count -f sam -r name -s no -a 10 -t gene -i gene_id -m intersection-nonempty %s %s > %s" % (sam, gtf, htseq_out))

# rm statistical information from htseq_out
# add colname to htseq_out
# output single cell dge
list_count = []
for cs in list_counts:
    prefix = re.sub('_counts.txt', '', cs)
    count_filename = prefix+'_count.txt'
    list_count.append(count_filename)

    file_counts = open(cs, 'r')
    file_count = open(count_filename,'w')
    counts_cont = file_counts.readlines()
    count_cont = counts_cont[:-5]
    file_count.write('GENE\t'+prefix+'\n')
    for line in count_cont:
        file_count.write(line)
    file_counts.close()
    file_count.close()
    print(cs+" finished!!!")
print("Finished!!!")

