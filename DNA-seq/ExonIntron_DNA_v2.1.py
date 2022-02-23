#!/usr/bin/env python
#coding=utf-8

import os
import re
import codecs
import argparse

parser = argparse.ArgumentParser(description='外显子比对率+内含子比对率(目录下所有_bwa.sorted.bam文件)：\
                                              python2 ExonIntron_DNA_v2.py \
                                              -e exon.bed \
                                              -g gene.bed ')

parser.add_argument('-e', '--exon', type=str, default='/home/songjia/reference/hg19/exon.bed', help='exon.bed')
parser.add_argument('-g', '--gene', type=str, default='/home/songjia/reference/hg19/gene.bed', help='gene.bed')

args = parser.parse_args()

def ExonIntron_DNA(bam, exon, gene):
    prefix=re.sub('.bwa.rmdup.bam','',bam)
    os.system("samtools depth %s.bwa.rmdup.bam > %s.bam.depth" %(prefix, prefix))
    os.system("samtools depth -b %s %s.bwa.rmdup.bam > %s_exon.bam.depth" %(exon, prefix, prefix))
    os.system("samtools depth -b %s %s.bwa.rmdup.bam > %s_gene.bam.depth" %(gene, prefix, prefix))

    file_ExonIntron=codecs.open(prefix+'_ExonIntron.txt','w')
    file_ExonIntron.write("Sample name: "+prefix+'\n')

    total_bases = 0
    file_total = open(prefix+'.bam.depth','r')
    for line in file_total:
        l = re.sub('\n','',line)
        f = int(l.split('\t')[2])
        total_bases = total_bases + f
    file_ExonIntron.write("Total mapped bases: "+str(total_bases)+'\n')
    file_total.close()
 
    exon_bases = 0
    file_exon = open(prefix+'_exon.bam.depth','r')
    for line in file_exon:
        l = re.sub('\n','',line)
        f = int(l.split('\t')[2])
        exon_bases = exon_bases + f
    p_exon = exon_bases / float(total_bases)
    file_ExonIntron.write("Exon bases: "+str(exon_bases)+'\n')
    file_ExonIntron.write("% of bases mapped to exon: {:.2%}".format(p_exon)+'\n')
    file_exon.close()
    
    gene_bases = 0
    file_gene = open(prefix+'_gene.bam.depth','r')
    for line in file_gene:
        l = re.sub('\n','',line)
        f = int(l.split('\t')[2])
        gene_bases = gene_bases + f
    p_gene = gene_bases / float(total_bases)
    p_intron = p_gene - p_exon
    file_ExonIntron.write("Gene bases: "+str(gene_bases)+'\n')
    file_ExonIntron.write("% of bases mapped to gene: {:.2%}".format(p_gene)+'\n')
    file_ExonIntron.write("% of bases mapped to intron: {:.2%}".format(p_intron)+'\n')
    file_exon.close()
    
    file_ExonIntron.close()
    print(bam+' is finished!')

exon = args.exon
gene = args.gene
os.system("ls *.bwa.rmdup.bam > list_EI_bam.txt")
file_list_bam = open('list_EI_bam.txt','r')
for i in file_list_bam:
    bam = re.sub('\n','',i)
    ExonIntron_DNA(bam, exon, gene)
file_list_bam.close()
os.system("rm list_EI_bam.txt")

