# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 14:31:14 2020

@author: cyclopenta
"""


import os

os.system('''mkdir lorenz''')
os.system('''ls *.rmdup.bam > temp_lorenz_file''')

with open('temp_lorenz_file', 'r')as REF:
    for line in REF:
        line = line.rstrip()
        file = line
        file_prefix = line.split('.')[0]
        os.system('''bam-lorenz-coverage -l {prefix}_table -L {prefix}_plot {finput};
                      mv {prefix}_table {prefix}_plot.png lorenz'''.format(prefix=file_prefix, finput=file))
os.system('rm temp_lorenz_file')
print('done')
