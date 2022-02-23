# -*- coding: utf-8 -*-
"""
Created on Thu May 13 19:02:27 2021

@author: cyclopenta
"""



import sys
import os
import re

#define parameters
f1 = str(sys.argv[1])
adapter_fasta = '/home/pipe_line/genomic_tools/adapters_DNA.fasta'
# read files with 1.fq
#os.popeen() will retrun a list of results of shell commands
f1 = f1.rstrip()
f2 = re.sub('1.fq','2.fq',f1)
prefix = f1.split('.fq')[0]
os.system(''' mkdir -p ./{path1}/trimed_reads_qc'''.format(path1 = prefix))
r1 = f1.split('.')[0]
r2 = f2.split('.')[0]
print('now processing: %s and %s'%(r1,r2))
os.system('''
cutadapt -q 20 -m 20 -j 10 -b file:{adapter} -n 2 -O 6 -e 0 -o {read1}_temp_1.fq {read1}.fq;
cutadapt -q 20 -m 20 -j 10 -b file:{adapter} -n 2 -O 6 -e 0 -o {read2}_temp_2.fq {read2}.fq;
cutadapt -q 20 -m 20 -j 10 -a "A{{30}}" -a "T{{30}}" -a "G{{30}}" -n 2 -O 30 -e 0 -o {read1}_trim_1.fq {read1}_temp_1.fq;
cutadapt -q 20 -m 20 -j 10 -a "A{{30}}" -a "T{{30}}" -a "G{{30}}" -n 2 -O 30 -e 0 -o {read2}_trim_2.fq {read2}_temp_2.fq;
/home/softwares/bbmap/repair.sh in1={read1}_trim_1.fq in2={read2}_trim_2.fq  out1={read1}_repair_1.fq out2={read2}_repair_2.fq;
rm {read1}_temp_1.fq {read2}_temp_2.fq {read1}_trim_1.fq {read2}_trim_2.fq;
fastqc -o ./{path1}/trimed_reads_qc -t 5 {read1}_repair_1.fq;
fastqc -o ./{path1}/trimed_reads_qc -t 5 {read2}_repair_2.fq;
mv {read1}_repair_1.fq {read2}_repair_2.fq ./{path1}'''.format(adapter = adapter_fasta,read1 = r1,read2 = r2,path1 = prefix )) 

print('cut & fastqc done!!!')
