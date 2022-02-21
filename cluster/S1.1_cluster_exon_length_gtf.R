# ！/usr/bin/R

# 根据参考基因组获得每条reads的exon length
# 参数：makeTxDbFromGFF()
library(GenomicFeatures)
txdb <- makeTxDbFromGFF("/home/songjia/reference/hg19/gencode.v35lift37.annotation.gtf",format="gtf")
exons_gene <- exonsBy(txdb, by = "gene")
exons_gene_lens <- lapply(exons_gene,function(x){sum(width(reduce(x)))})
n=t(as.data.frame(exons_gene_lens))
write.table(n,"cluster_exon_length_gtf.txt", sep = "\t", row.names = TRUE)

