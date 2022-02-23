# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 09:11:34 2021

@author: cyclopenta
"""


import os
import re
os.system('ls *.rmdup.bam>bam_to_bed.txt')
with open('bam_to_bed.txt', 'r')as ref:
    for line in ref:
        line = line.rstrip()
        file = line
        out_file = re.sub('.bam', '.bed', file)
        os.system('''bedtools bamtobed -i {0}>{1}
                      gzip -c {1}>{1}.gz
                      rm {1}'''.format(file, out_file))
os.system('rm bam_to_bed.txt')