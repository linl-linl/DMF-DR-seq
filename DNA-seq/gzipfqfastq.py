# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:40:37 2021

@author: cyclopenta
"""


# gzip fastq/fq

import os

os.system(' ls *.fastq> temp_gzip.txt')
os.system('ls *.fq>>temp_gzip.txt')

with open('temp_gzip.txt', 'r')as ref:
    for line in ref:
        line = line.rstrip()
        os.system('gzip -c {0}>{0}.gz'.format(line))
os.system('rm temp_gzip.txt')
print('done!')
