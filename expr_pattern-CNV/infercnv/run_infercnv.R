library(infercnv)
infercnv_obj = CreateInfercnvObject(raw_counts_matrix='./DGE_count.txt', annotations_file='./annotation_count.txt', delim="\t", gene_order_file="./gene_order.txt", ref_group_names=c('normal'))
infercnv_obj = infercnv::run(infercnv_obj, cutoff=1, out_dir=".", cluster_by_groups=T, denoise=T, HMM=F, output_format = "pdf")

