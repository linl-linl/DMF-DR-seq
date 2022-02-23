#!/usr/bin/env python
#coding=utf-8

import os
import re
import xlwt
import argparse

parser = argparse.ArgumentParser(description='整合各样本的ExonIntron信息: \
                                              python2 inf_ExonIntron.py \
                                              -o output')

parser.add_argument('-o', '--output', type=str, required=True, help='output_file_name')

args = parser.parse_args()

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("Sheet1")
sheet.write(0,0, '% of bases mapped to exon')
sheet.write(0,1, '% of bases mapped to intron')
sheet.write(0,2, '% of bases mapped to gene')
sheet.write(0,3, 'Exon bases')
sheet.write(0,4, 'Gene bases')
sheet.write(0,5, 'Total mapped bases')
sheet.write(0,6, 'Sample name')
count = 1
os.system("ls *_ExonIntron.txt > list_ExonIntron_tmp.txt")
file_list = open('list_ExonIntron_tmp.txt','r')
for i in file_list:
    m=re.sub('\n','',i)
    file_ExonIntron=open(m,'r')
    for i2 in file_ExonIntron:
        m2=re.sub('\n','',i2)
        n=m2.split(': ')
        if n[0] == 'Sample name':
            Sample_name = n[1]
        elif n[0] == 'Total mapped bases':
            Total_mapped_bases = n[1]
        elif n[0] == 'Exon bases':
            Exon_bases = n[1]
        elif n[0] == '% of bases mapped to exon':
            p_of_bases_mapped_to_exon = n[1]
        elif n[0] == 'Gene bases':
            Gene_bases = n[1]
        elif n[0] == '% of bases mapped to gene':
            p_of_bases_mapped_to_gene = n[1]
        elif n[0] == '% of bases mapped to intron':
            p_of_bases_mapped_to_intron = n[1]
    sheet.write(count,0, p_of_bases_mapped_to_exon)
    sheet.write(count,1, p_of_bases_mapped_to_intron)
    sheet.write(count,2, p_of_bases_mapped_to_gene)
    sheet.write(count,3, Exon_bases)
    sheet.write(count,4, Gene_bases)  
    sheet.write(count,5, Total_mapped_bases)
    sheet.write(count,6, Sample_name)
    count=count+1
file_list.close()
os.system("rm list_ExonIntron_tmp.txt")
workbook.save(args.output+'.xls')

