# Rscipt pic.R segcopy3 bounds
args=commandArgs(T)
library(ctc)
library(DNAcopy) # Segmentation
library(inline)  # Use of c++
library(gplots)  # Visual plotting of tables
library(scales)
library(plyr)
library(ggplot2)
library(gridExtra)

url = '/home/songjia/bigdisk/linl/xuxing_multiomics/RNA/expr_pattern2/test_3same_ref/DNA/'
segcopy = 'SegCopy'
file_bounds = 'DNA_bounds'

final=read.table(segcopy,header=T)
final=final[,4:dim(final)[2]]
final[final>8] = 8
top=8
l=dim(final)[1]
w=dim(final)[2]
bounds=read.table(file_bounds, header=F, sep='\t')
# rm XY for allbin
# bounds = bounds[1:(dim(bounds)[1]-2),]
# end_point = dim(bounds)[1]
# final=final[1:bounds[(dim(bounds)[1]),'V2'],]
# l=dim(final)[1]
# w=dim(final)[2]
pos=cbind(c(1,bounds[,2]), c(bounds[,2], l))
for(k in 1:w){
  # lowess.gc = function(jtkx, jtky) {
    # jtklow = lowess(jtkx, log(jtky), f=0.05);
    # jtkz = approx(jtklow$x, jtklow$y, jtkx)
    # return(exp(log(jtky) - jtkz$y))
  # }
  # final[,k] = lowess.gc(GC[,1],(final[,k]+1)/mean(final[,k]+1))

  pdf(file=paste(url, colnames(final)[k], "_CN.pdf", sep=""), width=75, height=30)

  rectangles1=data.frame(pos[seq(1,nrow(pos), 2),])
  rectangles2=data.frame(pos[seq(2,nrow(pos), 2),])
  amp=data.frame(x=which(final[,k]>2), y=final[which(final[,k]>2),k])
  del=data.frame(x=which(final[,k]<2), y=final[which(final[,k]<2),k])
  flat=data.frame(x=which(final[,k]==2), y=final[which(final[,k]==2),k])
  anno=data.frame(x=(pos[,2]+pos[,1])/2, y=-top*.05, chrom=substring(c(as.character(bounds[,1]),'chr'), 4 ,5))

  plot1 = ggplot() +
    geom_hline(yintercept = 2, color = '#999999', size=3) +
    geom_rect(data=rectangles1, aes(xmin=X1, xmax=X2, ymin=-top*.1, ymax=top), fill='gray85', alpha=0.75) +
    geom_rect(data=rectangles2, aes(xmin=X1, xmax=X2, ymin=-top*.1, ymax=top), fill='gray75', alpha=0.75) +
    geom_point(data=flat, aes(x=x, y=y), size=4) +
    geom_point(data=amp, aes(x=x, y=y), size=4, color='red') +
    geom_point(data=del, aes(x=x, y=y), size=4, color='blue') +
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
}
warnings()

