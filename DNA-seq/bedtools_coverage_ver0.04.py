# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 09:10:06 2020

@author: cyclopenta
"""
import os
from collections import defaultdict

# out_file will use /t to make table
out_file_name = 'coverage_stats.txt'
out_dict = defaultdict(tuple)
os.system('ls *rmdup.bam > bam_file_temp.txt')

with open('bam_file_temp.txt', 'r') as file_list:
    for f in file_list:
        f = f.rstrip()
        prefix = f.split('.bwa')[0]
        os.system(''' samtools index -@ 10 {bam_file};
                      bedtools genomecov -bga -ibam {bam_file}>{bed_file}_cov.bed'''.format(bam_file=f, bed_file=prefix))
# remove temp file
os.system('rm bam_file_temp.txt')
os.system('ls *_cov.bed > bed_file_temp.txt')
# info_list contains the information in every bed file
with open('bed_file_temp.txt', 'r') as ref:
    for f in ref:
        f = f.rstrip()
        length_dict = defaultdict(int)
        cov_dict = defaultdict(int)
        dep_dict = defaultdict(int)
        with open(f, 'r') as bedfile:
            for line in bedfile:
                line = line.rstrip()
                info_list = line.split()
                chrom = info_list[0]
                start_poi = int(info_list[1])
                end_poi = int(info_list[2])
        # refresh the end poi to record the chr lenght
                length_dict[chrom] = end_poi
                if 'e+' in info_list[3]:
                    cont = info_list[3].split('e+')
                    cont[1] = cont[1].lstrip('0')
                    cov_avg = int(float(cont[0]) * pow(10, int(cont[1])))
                else:
                    cov_avg = int(info_list[3])
                add_tmp = end_poi-start_poi
                add_dep_tmp = add_tmp*cov_avg
                if cov_avg:
                    cov_dict[chrom] += add_tmp
                dep_dict[chrom] += add_dep_tmp
        cov_dict = dict(cov_dict)
        length_dict = dict(length_dict)
        dep_dict = dict(dep_dict)
        cal_length = sum(length_dict.values())
        cal_cov = sum(cov_dict.values())
        cal_dep = sum(dep_dict.values())
        cov_acc = cal_cov/cal_length
        cov_eva = cal_cov/3000000000
        dep = cal_dep/cal_length
        out_dict[f] = (cov_acc, cov_eva, dep)
print('coverage cal and store done!')
out_dict = dict(out_dict)
os.system('rm bed_file_temp.txt')
with open(out_file_name, 'w') as OUT:
    col_list = ['file name', 'coverage(calculated by accurate length)', 'coverage(calculated by 3000Mbp length)', 'depth(calculated)']
    for col in col_list:
        str_tmp = col + '\t'
        OUT.write(str_tmp)
    OUT.write('\n')
    for key, val in out_dict.items():
        f_name = key.split('_cov')[0]
        w0 = f_name + '\t'
        w1 = str(val[0]) + '\t'
        w2 = str(val[1]) + '\t'
        w3 = str(val[2]) + '\n'
        line_str = w0 + w1 + w2 + w3
        OUT.write(line_str)
print('done')
