# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:48:53 2020

@author: cyclopenta
"""



import os

os.system('mkdir CV_FILE')
os.system('ls *bwa.rmdup.bam>cv_temp_file')

with open('cv_temp_file','r')as REF:
    for line in REF:
        line = line.rstrip()
        file = line
        out_prefix = line.split('.')[0]  
        os.system(''' samtools depth -a {infile} |awk -F $'\t' 'BEGIN {{OFS = FS}}{{sum += $3;}}(NR%1000000)==0{{print $1,$2 - 1000000,$2,sum;sum=0;}}' |awk '{{cnt++; Ssum=Ssum+$4*$4; sum=sum+$4;}}END{{std=sqrt((Ssum*cnt-sum*sum)/(cnt*(cnt-1)));
print "AVG:" sum/cnt; print "STD:"std;print "CV:"std*cnt/sum; print "Total Count:"cnt}}' > {prefix}_CV.txt;
              mv {prefix}_CV.txt CV_FILE;
              '''.format(infile = file, prefix = out_prefix)) 
    
os.system('''rm cv_temp_file''')

print('dong!')
