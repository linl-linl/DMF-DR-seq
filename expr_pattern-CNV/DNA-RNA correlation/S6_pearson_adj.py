# !usr/bin/env python
# -*- coding:utf-8 -*-

import os

file = open('nohup.out', 'r')
cont = file.readlines()
file.close()

out = open('pearson_adj.txt', 'w')
for i in range(0, len(cont)):
    if i < 12:
        out.write(cont[i])
    else:
        break
out.close()

#os.system('''rm nohup.out''')

