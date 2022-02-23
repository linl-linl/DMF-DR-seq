# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 11:15:40 2020

@author: cyclopenta
"""

import sys
import os
import re
import datetime

#define parameters
source_fasta_path = '/home/songjia/reference/hg19/hg19_latest.fa'
now_time = datetime.datetime.now()
time_str = now_time.strftime('%Y-%m-%d-%H_%M_%S')
bwa_out_path =time_str+'_bwa_out'
os.system(''' mkdir ./{path1}'''.format(path1 = bwa_out_path))
# read files with 1.fq
#os.popeen() will retrun a list of results of shell commands
os.system(' ls *_1_repair_1.fq > clean_file_bwa_temp.txt')

raw_file = open ('clean_file_bwa_temp.txt')

for f1 in raw_file:
    f1 = f1.rstrip()
    f2 = re.sub('_1_repair_1.fq','_2_repair_2.fq',f1)
    r1 = f1.split('.')[0]
    r2 = f2.split('.')[0]
    out_prefix = f1.split('_')[0]+'_'+f1.split('_')[1]
    print('now processing: %s and %s'%(r1,r2))
    os.system('''
bwa mem -t 10 -M -Y {fastapath} {read1}.fq {read2}.fq -o {prefix}_bwa.sam;
samtools view -b -@ 10 -o {prefix}_bwa.bam {prefix}_bwa.sam;
samtools sort -@ 10 -m 4G -O bam -o {prefix}_bwa.sorted.bam {prefix}_bwa.bam;
samtools rmdup -s {prefix}_bwa.sorted.bam {prefix}.bwa.rmdup.bam;
samtools flagstat {prefix}_bwa.sorted.bam >{prefix}_bwa_map;；
rm {prefix}_bwa.sorted.bam;
mv {prefix}_bwa.sam {prefix}_bwa.bam {prefix}_bwa.sorted.bam {prefix}_bwa_map {prefix}.bwa.rmdup.bam ./{path1};
'''.format(fastapath = source_fasta_path,read1 = r1,read2 = r2,path1 = bwa_out_path,prefix = out_prefix)) 
    
os.system('''rm clean_file_bwa_temp.txt''')

print('bwa map done!!!')

