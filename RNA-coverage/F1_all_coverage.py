import os

os.system("ls *.sorted.bam > list_sbam")
file = open('list_sbam', 'r')
for i in file:
    i = i.rstrip()
    os.system("samtools index -@ 20  %s" % (i))
    print(i+" index finished!")
file.close()
os.system("geneBody_coverage.py -r /home/songjia/reference/hg19/gencode.v35lift37.annotation.bed -i ./ -o all")
os.system("rm list_sbam")

