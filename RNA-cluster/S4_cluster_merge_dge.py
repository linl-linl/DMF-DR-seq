# ！usr/bin/env python
# -*- coding:utf-8 -*-

# 合并count.txt/fpkm.txt，生成表达矩阵，列名为样本名
# DGE_merge.py is required!!!

import os
import re
import argparse

def boolean_string(s):
    if s not in {'False', 'True'}:
        raise ValueError('Not a valid boolean string')
    return s == 'True'

parser = argparse.ArgumentParser(description='由目录下的Aligned.out.sam提取read counts，生成表达矩阵 \
                                              python cluster_merge_dge.py \
                                              -c True/False \
                                              -f True/False \
                                              -lc list_count \
                                              -lf list_fpkm')

parser.add_argument('-c', '--count', default=True, type=boolean_string, help='Bool type: True/False. merge count.txt to a dge')
parser.add_argument('-f', '--fpkm', default=True, type=boolean_string, help='Bool type: True/False.merge fpkm.txt to a dge')
parser.add_argument('-lc', '--listcount', type=str, default=0, help='a list of count.txt')
parser.add_argument('-lf', '--listfpkm', type=str, default=0, help='a list of fpkm.txt')

args = parser.parse_args()


if args.count:
    # save count_url to list_count
    if args.listcount:
        list_count = []
        file_count = open(args.listcount,'r')
        for i in file_count:
            count_name = re.sub('\n','',i)
            list_count.append(count_name)
    else:
        os.system("ls *_count.txt > list_count")
        list_count = []
        file_count = open('list_count', 'r')
        for i in file_count:
            count_url = re.sub('\n', '', i)
            list_count.append(count_url)
        os.system("rm list_count")

    # merge count_file to DGE
    lh = len(list_count)
    if (lh < 2):
        print("There is one count file!!!")
    elif (lh == 2):
        os.system("python DGE_merge.py -d1 %s -d2 %s" % (list_count[0], list_count[1]))
    
        file_anno = open('annotation_count.txt', 'w')
        file_dge = open('DGE_merge.txt', 'r')
        line1 = file_dge.readlines()[0]
        line1 = re.sub('\n', '', line1)
        ll = line1.split('\t')[1:]
        file_anno.write('SAMPLE\n')
        for sample_name in ll:
            file_anno.write(sample_name+'\n')
        file_anno.close()
        file_dge.close()
    else:
        os.system("python DGE_merge.py -d1 %s -d2 %s" % (list_count[0], list_count[1]))
        c = 2
        while (c < lh):
            os.system("python DGE_merge.py -d1 DGE_merge.txt -d2 %s" % (list_count[c]))
            c = c+1
        file_anno = open('annotation_count.txt', 'w')
        file_dge = open('DGE_merge.txt', 'r')
        line1 = file_dge.readlines()[0]
        line1 = re.sub('\n', '', line1)
        ll = line1.split('\t')[1:]
        file_anno.write('SAMPLE\n')
        for sample_name in ll:
            file_anno.write(sample_name+'\n')
        file_anno.close()
        file_dge.close()
    os.system("mv DGE_merge.txt DGE_count.txt")
    print("DGE_count.txt Finished!!!")

if args.fpkm:
    # save fpkm_url to list_fpkm
    if args.listfpkm:
        list_fpkm = []
        file_fpkm = open(args.listfpkm,'r')
        for i in file_fpkm:
            fpkm_name = re.sub('\n','',i)
            list_fpkm.append(fpkm_name)
    else:
        os.system("ls *_fpkm.txt > list_fpkm")
        list_fpkm = []
        file_fpkm = open('list_fpkm', 'r')
        for i in file_fpkm:
            fpkm_url = re.sub('\n', '', i)
            list_fpkm.append(fpkm_url)
        os.system("rm list_fpkm")

    # merge fpkm_file to DGE
    lh = len(list_fpkm)
    if (lh < 2):
        print("There is one fpkm file!!!")
    elif (lh == 2):
        os.system("python DGE_merge.py -d1 %s -d2 %s" % (list_fpkm[0], list_fpkm[1]))

        file_anno = open('annotation_fpkm.txt', 'w')
        file_dge = open('DGE_merge.txt', 'r')
        line1 = file_dge.readlines()[0]
        line1 = re.sub('\n', '', line1)
        ll = line1.split('\t')[1:]
        file_anno.write('SAMPLE\n')
        for sample_name in ll:
            file_anno.write(sample_name+'\n')
        file_anno.close()
        file_dge.close()
    else:
        os.system("python DGE_merge.py -d1 %s -d2 %s" % (list_fpkm[0], list_fpkm[1]))
        c = 2
        while (c < lh):
            os.system("python DGE_merge.py -d1 DGE_merge.txt -d2 %s" % (list_fpkm[c]))
            c = c+1
        file_anno = open('annotation_fpkm.txt', 'w')
        file_dge = open('DGE_merge.txt', 'r')
        line1 = file_dge.readlines()[0]
        line1 = re.sub('\n', '', line1)
        ll = line1.split('\t')[1:]
        file_anno.write('SAMPLE\n')
        for sample_name in ll:
            file_anno.write(sample_name+'\n')
        file_anno.close()
        file_dge.close()
    os.system("mv DGE_merge.txt DGE_fpkm.txt")
    print("DGE_fpkm.txt Finished!!!")

print("Finished!!!")

