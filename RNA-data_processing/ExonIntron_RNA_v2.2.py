#!/usr/bin/env python
#coding=utf-8

import os
import re
import codecs
import argparse

parser = argparse.ArgumentParser(description='外显子比对率+内含子比对率(对目录下所有Aligned.out.sam文件操作)：\
                                              python2 ExonIntron_RNA_v2.py \
                                              -e exon.bed \
                                              -g gene.bed ')

parser.add_argument('-e', '--exon', type=str, default='/home/songjia/reference/hg19/exon.bed', help='exon.bed')
parser.add_argument('-g', '--gene', type=str, default='/home/songjia/reference/hg19/gene.bed', help='gene.bed')

args = parser.parse_args()


def ExonIntron_RNA(sam, exon, gene):
    prefix=re.sub('Aligned.out.sam','',sam)
    os.system("samtools view -@ 15 -bS %s > %s.bam" %(sam, prefix))
    os.system("samtools sort -@ 15 %s.bam -o %s.sorted.bam" %(prefix, prefix))
    os.system("samtools depth %s.sorted.bam > %s.bam.depth" %(prefix, prefix))
    os.system("samtools depth -b %s %s.sorted.bam > %s_exon.bam.depth" %(exon, prefix, prefix))
    os.system("samtools depth -b %s %s.sorted.bam > %s_gene.bam.depth" %(gene, prefix, prefix))

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
    file_gene.close()
    
    file_ExonIntron.close()
    os.system("rm %s.bam" % (prefix))
    os.system("rm %s.bam.depth" % (prefix))
    os.system("rm %s_exon.bam.depth" % (prefix))
    os.system("rm %s_gene.bam.depth" % (prefix))
    print(sam+' is finished!')

exon = args.exon
gene = args.gene
os.system("ls *Aligned.out.sam > list_Aligned_out_sam.txt")
file_list_sam = open('list_Aligned_out_sam.txt','r')
for i in file_list_sam:
    sam = re.sub('\n','',i)
    ExonIntron_RNA(sam, exon, gene)
file_list_sam.close()
os.system("rm list_Aligned_out_sam.txt")

