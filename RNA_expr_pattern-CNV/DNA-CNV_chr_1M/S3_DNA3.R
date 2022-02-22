# Rscript chr_average.R sample_name

args = commandArgs(T)

library(ctc)
library(DNAcopy)  # Segmentation
library(inline)  # Use of c++
library(gplots)  # Visual plotting of tables
library(scales)
library(plyr)
library(ggplot2)
library(gridExtra)

url = '/home/songjia/bigdisk/linl/xuxing_multiomics/RNA/expr_pattern2/test_3same_ref/DNA_chr_1M/'
segcopy2 = paste(args[1], '_SegCopy2', sep='')
file_bounds = 'DNA_bounds'

final = read.table(segcopy2, header=T)
# final[final>3] = 3
final[final>8] = 8
top = 8
coln = length(colnames(final))
if (coln == 4){
    colnames(final) = c('A', 'B', 'C', 'Average')
    final$num = as.numeric(rownames(final))
}else if (coln == 5){
    colnames(final) = c('A', 'B', 'C', 'D', 'Average')
    final$num = as.numeric(rownames(final))
}else if (coln == 6){
    colnames(final) = c('A', 'B', 'C', 'D', 'E', 'Average')
    final$num = as.numeric(rownames(final))
}else if (coln == 7){
    colnames(final) = c('A', 'B', 'C', 'D', 'E', 'F', 'Average')
    final$num = as.numeric(rownames(final))
}
l=dim(final)[1]
w=dim(final)[2]-1
bounds = read.table(file_bounds, header=F, sep='\t')
pos = cbind(c(1, bounds[, 2]), c(bounds[, 2], l))

# rectangles1 = data.frame(pos[seq(1, nrow(pos), 2), ])
# rectangles2 = data.frame(pos[seq(2, nrow(pos), 2), ])
# anno = data.frame(x=(pos[, 2]+pos[, 1])/2, y=-top*.05, chrom=substring(c(as.character(bounds[, 1]), 'chr'), 4, 5))
for (i in (1: 22)){
    if (i == 1){
        s = 1
    }else{
        s = bounds[, 2][i-1]
    }
    e = bounds[, 2][i]
    dd = final[s:e, ]
    dd$num = (1:dim(dd)[1])
    dd$num = dd$num*1000000
    s2 = 0-(e-s)*0.05*1000000
    e2 = (dim(dd)[1]+(e-s)*0.05)*1000000
    amp = data.frame(x=(which(dd[,'Average']>2)*1000000), y=dd[which(dd[,'Average']>2),'Average'])
    del = data.frame(x=(which(dd[,'Average']<2)*1000000), y=dd[which(dd[,'Average']<2),'Average'])
    flat = data.frame(x=(which(dd[,'Average']==2)*1000000), y=dd[which(dd[,'Average']==2),'Average'])
    pdf(file=paste(url, args[1], "_CN_chr", i, ".pdf", sep=""), width=5, height=2)
    plot1 = ggplot() + geom_hline(yintercept = 2, color = '#999999', size=1)
    if (coln >= 4){
        plot1 = plot1 + 
            geom_point(data=dd, aes(x=num, y=A), size=1, color="grey") +
            geom_point(data=dd, aes(x=num, y=B), size=1, color="grey") +
            geom_point(data=dd, aes(x=num, y=C), size=1, color="grey")
    }
    if (coln >= 5){
        plot1 = plot1 + geom_point(data=dd, aes(x=num, y=D), size=1, color="grey")
    }
    if (coln >= 6){
        plot1 = plot1 + geom_point(data=dd, aes(x=num, y=E), size=1, color="grey")
    }
    if (coln >= 7){
        plot1 = plot1 + geom_point(data=dd, aes(x=num, y=F), size=1, color="grey")
    }
    plot1 = plot1 +     
        geom_point(data=flat, aes(x=x, y=y), size=1) +
        geom_point(data=amp, aes(x=x, y=y), size=1, color='red') +
        geom_point(data=del, aes(x=x, y=y), size=1, color='blue') +
        scale_x_continuous(limits=c(s2, e2), expand = c(0, 0)) +
        scale_y_continuous(limits=c(-top*.1, top*1.1), expand = c(0, 0)) +
        labs( title='',x="Genomic position", y="DNA-CNV", size=60) +
        #theme(plot.title=element_text(size=40, vjust=1.5,face='bold')) +
        theme(axis.title.x=element_text(size=100, vjust=-.05,face='bold'), axis.title.y=element_text(size=100, vjust=.05,face='bold')) +
        theme(axis.text=element_text(color="black", size=130,face='bold'), axis.ticks=element_line(color="black"))+
        theme(axis.ticks.x = element_blank(), axis.text.x = element_blank(), axis.line.x = element_blank()) +
        #theme(panel.background = element_rect(fill = 'gray90')) +
        theme(plot.margin=unit(c(.5,1,.5,1),"cm")) +
        #theme(panel.grid.major.x = element_blank()) + geom_vline(xintercept = c(1, l), size=.5) +
        theme_bw()
    print(plot1)
    dev.off()
}

warnings()

