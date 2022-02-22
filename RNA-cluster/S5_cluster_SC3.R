library(scater)
library(SingleCellExperiment)
library(SC3)
data <- read.table("DGE_fpkm.txt", header = T, row.names = 1)
data2 <- read.table("annotation_fpkm.txt", header = T)
data3 <- t(data)
sce <- SingleCellExperiment(assays = list(counts = as.matrix(t(data3)),logcounts =log2(as.matrix(t(data3))+1)), colData = data2)
rowData(sce)$feature_symbol <- rownames(sce)
sce <- sce[!duplicated(rowData(sce)$feature_symbol), ]

sce <- sc3_estimate_k(sce)
sce@metadata$sc3$k_estimation

sce <- sc3(sce, ks = 3:5, biology = TRUE, gene_filter=T, n_cores=10)
sc3_plot_expression(sce, k = 3, show_pdata = c("CELL","GROUP"))
sc3_plot_expression(sce, k = 3, show_pdata = c("SAMPLE_M","SAMPLE_H","SAMPLE_S"))

sce2 <- sce[sce@rowRanges@elementMetadata@listData[["sc3_gene_filter"]]=='TRUE',]

sce2 <- runPCA(sce2)
plotPCA(sce2, colour_by = "CELL")
sce2 <- runTSNE(sce2)
plotTSNE(sce2, colour_by = "CELL")
sce2 <- runUMAP(sce2)
plotUMAP(sce2, colour_by = "CELL")
