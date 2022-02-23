# -*- coding: utf-8 -*-
"""
Created on Thu May 13 19:51:21 2021

@author: cyclopenta
"""


import sys
import os
import re

#define parameters
source_fasta_path = str(sys.argv[1])
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
/home/softwares/bwa-0.7.17/bwa mem -t 10 -M -Y {fastapath} {read1}.fq {read2}.fq -o {prefix}_bwa.sam;
/usr/local/bin/samtools view -b -@ 10 -o {prefix}_bwa.bam {prefix}_bwa.sam;
/usr/local/bin/samtools sort -@ 10 -m 4G -O bam -o {prefix}_bwa.sorted.bam {prefix}_bwa.bam;
/usr/local/bin/samtools rmdup -s {prefix}_bwa.sorted.bam {prefix}.bwa.rmdup.bam;
/usr/local/bin/samtools flagstat {prefix}_bwa.rmdup.bam >{prefix}_bwa_map;；
rm {prefix}_bwa.sorted.bam;
'''.format(fastapath = source_fasta_path,read1 = r1,read2 = r2,prefix = out_prefix)) 
    
os.system('''rm clean_file_bwa_temp.txt''')

print('bwa map done!!!')

