import os
import re

gtf = '/home/songjia/reference/hg19/gencode.v35lift37.annotation.gtf'
os.system("ls *_counts.txt > list_counts")
file = open('list_counts', 'r')
for i in file:
    i = i.rstrip()
    # 去除 readcount 为0的 "gene    readcount"
    os.system("python GeneReadCount.py -f %s" % (i))
    # "gene    readcount" 降序排序
    i2 = re.sub('_counts.txt', '_GeneReadCount.txt', i)
    os.system("python CountFilter.py -f %s" % (i2))
    # 由top1k/middle1k/bottom1k里的gene过滤gtf文件
    t = re.sub('.txt', '_top1000.txt', i)
    m = re.sub('.txt', '_middle1000.txt', i)
    b = re.sub('.txt', '_bottom1000.txt', i)
    os.system("python GtfFilter.py -f %s -g %s" % (t, gtf))
    os.system("python GtfFilter.py -f %s -g %s" % (m, gtf))
    os.system("python GtfFilter.py -f %s -g %s" % (b, gtf))
    # 将gtf文件转化为bed文件
    it = re.sub('.txt', '_new.gtf', t)
    im = re.sub('.txt', '_new.gtf', m)
    ib = re.sub('.txt', '_new.gtf', b)
    ot = re.sub('.txt', '_new.bed', t)
    om = re.sub('.txt', '_new.bed', m)
    ob = re.sub('.txt', '_new.bed', b)
    os.system("~/software/ea-utils-master--gtf2bed/clipper/gtf2bed %s > %s" % (it, ot))
    os.system("~/software/ea-utils-master--gtf2bed/clipper/gtf2bed %s > %s" % (im, om))
    os.system("~/software/ea-utils-master--gtf2bed/clipper/gtf2bed %s > %s" % (ib, ob))
    # 作图
    ibam = re.sub('_counts.txt', '.sorted.bam', i)
    r = ot
    o = re.sub('_counts', '', r)
    o = re.sub('_new.bed', '', o)
    os.system("geneBody_coverage.py -r %s -i %s -o %s" % (r, ibam, o))
    r = om
    o = re.sub('_counts', '', r)
    o = re.sub('_new.bed', '', o)
    os.system("geneBody_coverage.py -r %s -i %s -o %s" % (r, ibam, o))
    r = ob
    o = re.sub('_counts', '', r)
    o = re.sub('_new.bed', '', o)
    os.system("geneBody_coverage.py -r %s -i %s -o %s" % (r, ibam, o))
file.close()
os.system("rm list_counts")

