# Rscipt pic.R file_url
args=commandArgs(T)
library(ctc)
library(DNAcopy) # Segmentation
library(inline)  # Use of c++
library(gplots)  # Visual plotting of tables
library(scales)
library(plyr)
library(ggplot2)
library(gridExtra)

url = '/home/songjia/bigdisk/linl/xuxing_multiomics/RNA/expr_pattern2/test_3same_ref/'
#segcopy4 = paste(args[1], '/segcopy4', sep='')
#file_bounds = paste(args[1], '/bounds', sep='')
# allbin
segcopy4 = paste(args[1], '/segcopy5', sep='')
file_bounds = paste(args[1], '/bounds_allbin', sep='')

#final=read.table(segcopy4,header=T)
# allbin
final=read.table(segcopy4,header=T,row.names=1,sep='\t')
l=dim(final)[1]
w=dim(final)[2]-1
bounds=read.table(file_bounds, header=F, sep='\t')
# rm XY for allbin
bounds = bounds[1:(dim(bounds)[1]-2),]
end_point = dim(bounds)[1]
final=final[1:bounds[(dim(bounds)[1]),'V2'],]
l=dim(final)[1]
w=dim(final)[2]
pos=cbind(c(1,bounds[,2]), c(bounds[,2], l))

pdf(file=paste(url, args[1], "_CN.pdf", sep=""), width=75, height=30)
dd=final
coln = length(colnames(final))
if (coln == 4){
    colnames(dd) = c('A', 'B', 'C', 'Average')
}else if (coln == 5){
    colnames(dd) = c('A', 'B', 'C', 'D', 'Average')
}else if (coln == 6){
    colnames(dd) = c('A', 'B', 'C', 'D', 'E', 'Average')
}else if (coln == 7){
    colnames(dd) = c('A', 'B', 'C', 'D', 'E', 'F', 'Average')
}
dd$num=as.numeric(rownames(final))
top=3
rectangles1=data.frame(pos[seq(1,nrow(pos), 2),])
rectangles2=data.frame(pos[seq(2,nrow(pos), 2),])
anno=data.frame(x=(pos[,2]+pos[,1])/2, y=-top*.05, chrom=substring(c(as.character(bounds[,1]),'chr'), 4 ,5))
plot1 = ggplot() +
  geom_rect(data=rectangles1, aes(xmin=X1, xmax=X2, ymin=-top*.1, ymax=top), fill='gray85', alpha=0.75) +
  geom_rect(data=rectangles2, aes(xmin=X1, xmax=X2, ymin=-top*.1, ymax=top), fill='gray75', alpha=0.75)
  if (coln >= 4){
        plot1 = plot1 + 
            geom_point(data=dd, aes(x=num, y=A), size=6, color='#999999') +
            geom_point(data=dd, aes(x=num, y=B), size=6, color='#999999') +
            geom_point(data=dd, aes(x=num, y=C), size=6, color='#999999')
    }
    if (coln >= 5){
        plot1 = plot1 + geom_point(data=dd, aes(x=num, y=D), size=6, color='#999999')
    }
    if (coln >= 6){
        plot1 = plot1 + geom_point(data=dd, aes(x=num, y=E), size=6, color='#999999')
    }
    if (coln >= 7){
        plot1 = plot1 + geom_point(data=dd, aes(x=num, y=F), size=6, color='#999999')
    }
  plot1 = plot1 + 
  geom_point(data=dd, aes(x=num, y=Average, color=Average), size=8) +
  scale_color_gradient2(midpoint=1, low="blue", mid="black", high="red") +
  geom_text(data=anno, aes(x=x, y=y, label=chrom), size=18,fontface='bold') +
  scale_x_continuous(limits=c(0, l), expand = c(0, 0)) +
  scale_y_continuous(limits=c(-top*.1, top), expand = c(0, 0)) +
  labs( title='',x="Chromosome", y="Copy Number", size=26) +
  theme(plot.title=element_text(size=40, vjust=1.5,face='bold')) +
  theme(axis.title.x=element_text(size=75, vjust=-.05,face='bold'), axis.title.y=element_text(size=75, vjust=.05,face='bold')) +
  theme(axis.text=element_text(color="black", size=75,face='bold'), axis.ticks=element_line(color="black"))+
  theme(axis.ticks.x = element_blank(), axis.text.x = element_blank(), axis.line.x = element_blank()) +
  theme(panel.background = element_rect(fill = 'gray90')) +
  theme(plot.margin=unit(c(.5,1,.5,1),"cm")) +
  theme(panel.grid.major.x = element_blank()) + geom_vline(xintercept = c(1, l), size=.5) +
  geom_hline(yintercept = c(-top*.1, top), size=.5)

grid.arrange(plot1, ncol=1)

dev.off()
warnings()
