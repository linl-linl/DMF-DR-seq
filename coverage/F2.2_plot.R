library(tidyr)
library(ggplot2)

# filenames
SKBR3 = c('0729RNA1_L2','0729RNA2_L2','0804RNA1_L3','0804RNA2_L3','0805RNA1_L3','0921RNA2_L4','1000-1_L3','1000-2_L3','1000_L3','1029RNA1_L3','1029RNA2_L1','1111RNA1_L1','1111RNA2_L2')
MCF7 = c('0107RNA1_L2','0107RNA2_L2','0126RNA1_L2','0126RNA4_L2','0201RNA1_L1','1022RNA1_L4','1022RNA2_L4','1201RNA1_L3','HR-1_L3','HR-2_L3','HR_L2')
HCT116 = c('0916RNA2_L2','0916RNA2_L3','0923RNA1_L4','0923RNA3_L4','0923RNA4_L4','1014RNA','1205RNA3_L1','MR-1_L3','MR-2_L2','MR_L2')
sample = HCT116
sample_top = paste(sample,'top1000.geneBodyCoverage.txt',sep='_')
sample_middle = paste(sample,'middle1000.geneBodyCoverage.txt',sep='_')
sample_bottom = paste(sample,'bottom1000.geneBodyCoverage.txt',sep='_')

# data_geneBodyCoverage
list_top = list()
for (i in 1:length(sample_top)){
    data = read.table(file = sample_top[i], header = T, row.names= 1)
    data[1,] = data[1,]/max(data[1,])
    list_top[[i]] = data
}
data_top = do.call(rbind, list_top)

list_middle <- list()
for (i in 1:length(sample_middle)){
    data <- read.table(file = sample_middle[i], header = T, row.names= 1)
    data[1,] = data[1,]/max(data[1,])
    list_middle[[i]] = data
}
data_middle = do.call(rbind, list_middle)

list_bottom <- list()
for (i in 1:length(sample_bottom)){
    data <- read.table(file = sample_bottom[i], header = T, row.names= 1)
    data[1,] = data[1,]/max(data[1,])
    list_bottom[[i]] = data
}
data_bottom = do.call(rbind, list_bottom)

anno = read.table('/home/songjia/newdisk/xuxing_multiomics/RNA/coverage/annotation.txt',header=T,row.names=1)

# adjust data
data_top$Sample = rownames(data_top)
data_top$Sample = do.call(rbind,strsplit(data_top$Sample,split='V'))[,2]
data_top$Sample = do.call(rbind,strsplit(data_top$Sample,split='.sorted'))[,1]
data_top = gather(data_top, Percentile, Coverage, -Sample)
data_top$Percentile = as.numeric(do.call(rbind,strsplit(data_top[,'Percentile'],split='X'))[,2])
data_top$Group = rep('g', dim(data_top)[1])
for (i in 1:dim(data_top)[1]){
    cell=data_top[i,'Sample']
    data_top[i,'Group']=as.character(anno[cell,'GROUP'])
}

data_middle$Sample = rownames(data_middle)
data_middle$Sample = do.call(rbind,strsplit(data_middle$Sample,split='V'))[,2]
data_middle$Sample = do.call(rbind,strsplit(data_middle$Sample,split='.sorted'))[,1]
data_middle = gather(data_middle, Percentile, Coverage, -Sample)
data_middle$Percentile = as.numeric(do.call(rbind,strsplit(data_middle[,'Percentile'],split='X'))[,2])
data_middle$Group = rep('g', dim(data_middle)[1])
for (i in 1:dim(data_middle)[1]){
    cell=data_middle[i,'Sample']
    data_middle[i,'Group']=as.character(anno[cell,'GROUP'])
}

data_bottom$Sample = rownames(data_bottom)
data_bottom$Sample = do.call(rbind,strsplit(data_bottom$Sample,split='V'))[,2]
data_bottom$Sample = do.call(rbind,strsplit(data_bottom$Sample,split='.sorted'))[,1]
data_bottom = gather(data_bottom, Percentile, Coverage, -Sample)
data_bottom$Percentile = as.numeric(do.call(rbind,strsplit(data_bottom[,'Percentile'],split='X'))[,2])
data_bottom$Group = rep('g', dim(data_bottom)[1])
for (i in 1:dim(data_bottom)[1]){
    cell=data_bottom[i,'Sample']
    data_bottom[i,'Group']=as.character(anno[cell,'GROUP'])
}

write.table(data_top,'data_top.txt',row.names=T,col.names=T,sep='\t')
write.table(data_middle,'data_middle.txt',row.names=T,col.names=T,sep='\t')
write.table(data_bottom,'data_bottom.txt',row.names=T,col.names=T,sep='\t')

# plot
pdf('Coverage_top1000.pdf',width=6,height=5)
ggplot(data_top,aes(x=Percentile,y=Coverage,group=Sample))+geom_line(aes(color=Group),size=1)+xlab("Gene body percentile (5' -> 3')")+ylab("Relative coverage (0 -> 1)")+theme_bw()
dev.off()

pdf('Coverage_middle1000.pdf',width=6,height=5)
ggplot(data_middle,aes(x=Percentile,y=Coverage,group=Sample))+geom_line(aes(color=Group),size=1)+xlab("Gene body percentile (5' -> 3')")+ylab("Relative coverage (0 -> 1)")+theme_bw()
dev.off()

pdf('Coverage_bottom1000.pdf',width=6,height=5)
ggplot(data_bottom,aes(x=Percentile,y=Coverage,group=Sample))+geom_line(aes(color=Group),size=1)+xlab("Gene body percentile (5' -> 3')")+ylab("Relative coverage (0 -> 1)")+theme_bw()
dev.off()


