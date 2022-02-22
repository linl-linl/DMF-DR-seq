# !usr/bin/env python
# -*- coding:utf-8 -*-

import os

file = open('nohup.out', 'r')
cont = file.readlines()
file.close()

out = open('pearson_record.txt', 'w')
for i in range(0, len(cont)):
    if "Pearson's product-moment correlation" in cont[i]:
        out.write('\n')
        out.write(cont[i]+cont[i+1]+cont[i+2]+cont[i+3]+cont[i+4]+cont[i+5]+cont[i+6]+cont[i+7]+cont[i+8]+cont[i+9])
        out.write('\n')
out.close()

#os.system('''rm nohup.out''')

