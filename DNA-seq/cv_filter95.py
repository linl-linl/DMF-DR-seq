# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 09:16:46 2021

@author: cyclopenta
"""

import os
import time
import pandas as pd
# 0-95% bins
begin_time = time.time()
os.system('mkdir CV_FILE_modified')
os.system('ls *bwa.rmdup.bam>filtered_cv_temp_file')

with open('filtered_cv_temp_file', 'r')as REF:
    for line in REF:
        line = line.rstrip()
        file = line
        out_prefix = line.split('.')[0]
        os.system(''' samtools depth -a {infile} |awk -F $'\t' 'BEGIN {{OFS = FS}}{{sum += $3;}}(NR%1000000)==0{{print $1,$2 - 1000000,$2,sum;sum=0;}}' > {prefix}_bin_f.txt;
              '''.format(infile = file, prefix = out_prefix)) 
        binfile = out_prefix + '_bin_f.txt'
        df = pd.read_csv(binfile, sep='\t', header = None)
        df = df.sort_values(by = 3)
        df_len = len(df[0])
        df_filter = df_len*0.95
        df.reset_index(drop=True, inplace=True)
        df_filtered = df[df.index.values+1<df_filter]
        df_out = df_filtered.describe()
        df_mean = df_out.iloc[1,2]
        df_std = df_out.iloc[2,2]
        df_count = df_out.iloc[0,2]
        df_CV = df_std/df_mean
        with open (out_prefix + '_filteredCV.txt', 'w')as OUT:
            str_tmp = 'AVG:' + str(df_mean) + '\n'
            str_tmp += 'STD:' + str(df_std) + '\n'
            str_tmp += 'CV:' + str(df_CV) + '\n'
            str_tmp += 'Total Count:' + str(df_count)
            OUT.write(str_tmp)
        os.system('rm {prefix}_bin_f.txt'.format(prefix = out_prefix))
        os.system('mv {prefix}_filteredCV.txt CV_FILE_modified'.format(prefix = out_prefix))
print(df_mean, df_std, df_CV)
os.system('''rm cv_temp_file''')
print('done!')
end_time = time.time()
run_time = float(end_time-begin_time)/60.0
print(run_time)