#!/usr/bin/env python
#coding=utf-8

##python2 xls_read.py file.xls

import sys
import re
import xlrd

# 打开excel文件
data = xlrd.open_workbook(sys.argv[1])
# 查看sheet，根据sheet名字来获取excel中的sheet
print("sheets：" + str(data.sheet_names()))
name_or_index = raw_input('Enter the sheet name or index(n or i):\n')
if name_or_index == 'n':
    by_name = input('Enter the sheet name:\n')
    table = data.sheet_by_name(by_name)
elif name_or_index == 'i':
    by_index = input('Enter the sheet index:\n')
    table = data.sheet_by_index(by_index)
else:
    print('Input Error!')
# 获取行数和列数
nrows=table.nrows
ncols=table.ncols

# 某一行数据
txt = raw_input('Do you want to output the sheet to a txt file(y or n):\n')
if txt == 'y':
    prefix=re.sub('.xls','',sys.argv[1])
    file=open(prefix+'.txt','w')
    list=[]
    for rnum in range(0,nrows):
        row=table.row_values(rnum)
        list.append(row)
    for p in list:
        line=''
        for q in p:
            line=line+q+'\t'
        line=line.rstrip()+'\n'
        file.write(line)
    file.close()
elif txt == 'n':
    for rnum in range(0,nrows):
        row=table.row_values(rnum)
        print(row)
