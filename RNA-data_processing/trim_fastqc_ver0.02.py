# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 17:24:13 2020

@author: cyclopenta
"""


import pandas as pd
import sys
import os
import re
import datetime

#define parameters
adapter_fasta = 'adapters_RNA.fasta'
now_time = datetime.datetime.now()
time_str = now_time.strftime('%Y-%m-%d-%H_%M_%S')
trim_path = time_str+'_trim_and_fastqc'
fastqc_out_path =time_str+'_fastqc_out'
os.system(''' mkdir -p ./{path1}/{path2}'''.format(path1 = trim_path, path2 = fastqc_out_path))
# read files with 1.fq
#os.popeen() will retrun a list of results of shell commands
os.system(' ls *1.fq > raw_file_temp.txt')

raw_file = open ('raw_file_temp.txt')

for f1 in raw_file:
    f1 = f1.rstrip()
    f2 = re.sub('1.fq','2.fq',f1)
    r1 = f1.split('.')[0]
    r2 = f2.split('.')[0]
    print('now processing: %s and %s'%(r1,r2))
    os.system('''
cutadapt -q 20 -m 20 -j 20 -b file:{adapter} -n 2 -O 6 -e 0 -o {read1}_temp_1.fq {read1}.fq;
cutadapt -q 20 -m 20 -j 20 -b file:{adapter} -n 2 -O 6 -e 0 -o {read2}_temp_2.fq {read2}.fq;
cutadapt -q 20 -m 20 -j 20 -a "A{{30}}" -a "T{{30}}" -a "G{{30}}" -n 2 -O 30 -e 0 -o {read1}_trim_1.fq {read1}_temp_1.fq;
cutadapt -q 20 -m 20 -j 20 -a "A{{30}}" -a "T{{30}}" -a "G{{30}}" -n 2 -O 30 -e 0 -o {read2}_trim_2.fq {read2}_temp_2.fq;
repair.sh in1={read1}_trim_1.fq in2={read2}_trim_2.fq  out1={read1}_repair_1.fq out2={read2}_repair_2.fq;
rm {read1}_temp_1.fq {read2}_temp_2.fq {read1}_trim_1.fq {read2}_trim_2.fq;
fastqc -o ./{path1}/{path2} -t 5 {read1}_repair_1.fq;
fastqc -o ./{path1}/{path2} -t 5 {read2}_repair_2.fq;'''.format(adapter = adapter_fasta,read1 = r1,read2 = r2,path1 = trim_path,path2 = fastqc_out_path  )) 
    
os.system('''rm raw_file_temp.txt''')

os.system('''ls *repair_*.fq > file_repair.txt''')

out_list = open ('file_repair.txt')

for f in out_list:
    f = f.rstrip()
    os.system('''mv {out} ./{path1}'''.format(out = f,path1 = trim_path ))
    
os.system('''rm file_repair.txt''')

print('cut & fastqc done!!!')
