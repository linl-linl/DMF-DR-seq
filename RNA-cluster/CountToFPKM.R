# 导入所有reads的count值，header = T保证后续计算不会将列名算入而造成错误
args = commandArgs(T)
filein = args[1]
fileout = args[2]
n <- read.table(file="cluster_exon_length_gtf_fadj.txt", header = T, row.names = 1)
count1 <- read.table(file=filein, row.names = 1, header = T)

countToFpkm <- function(counts, effLen)
{
    N <- sum(counts)
    exp( log(counts) + log(1e9) - log(effLen) - log(N) )
}

count5 <- mapply(countToFpkm, count1, n)
count5 <- data.frame(count5)
rn5 <- rownames(count1)
rownames(count5) <- rn5

# 生成表格
write.table(count5, fileout, row.names = TRUE, col.names = FALSE, sep = '\t')

