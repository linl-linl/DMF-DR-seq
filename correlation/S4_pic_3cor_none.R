args=commandArgs(T)

# Rscrpit pic_3cor_none.R output_of_Gfilter_3cor_none.py count/fpkm

library("ggplot2")


out_cor <- function(corh){
    out=paste('    ',as.character(corh$method),sep='')
    out=paste(out,'data:\t',sep='\n\n')
    out=paste(out,as.character(corh$data.name),sep='')
    out=paste(out,'t = ',sep='\n')
    out=paste(out,as.character(corh$statistic['t']),',',' df = ',as.character(corh$parameter['df']),',',' p-value < ',sep='')
    p=corh$p.value
    if (p==0){
        p='2.2e-16'
    }else{
        p=format(corh$p.value,scientific=TRUE,digit=4)
    }
    out=paste(out,p,sep='')
    out=paste(out,'alternative:\t',sep='\n')
    out=paste(out,as.character(corh$alternative),sep='')
    out=paste(out,'alternative hypothesis: true correlation is not equal to ',sep='\n')
    out=paste(out,as.character(corh$null.value['correlation']),sep='')
    out=paste(out,'95 percent confidence interval:\n',sep='\n')
    out=paste(out,as.character(corh$conf.int)[1],as.character(corh$conf.int)[2],sep='    ')
    out=paste(out,'sample estimates:\n\tcor\n',sep='\n')
    out=paste(out,as.character(corh$estimate),sep='    ')
    out=paste(out,'\n',sep='')
    return(out)
}


file=args[1]  # output of Gfilter_2cor.py
expr=args[2]  # count/fpkm
nfiltern=strsplit(strsplit(file, split='_')[[1]][2], split='.txt')[[1]][1]
data=read.table(file,header=T,row.names=1,sep='\t')
data$p1=log(data[,1]+0.25)/log(2)
data$p2=log(data[,2]+0.25)/log(2)
data$p3=log(data[,3]+0.25)/log(2)

colnames(data)[1:2]
cor.test(data$p1,data$p2)
corh=cor.test(data$p1,data$p2)
outcor=out_cor(corh)
outtxt=paste(colnames(data)[1],'_',colnames(data)[2],'_',nfiltern,'_cor.txt',sep='')
write(outcor,file=outtxt)

outpdf=paste(colnames(data)[1],'_',colnames(data)[2],'_',nfiltern,'_cor.pdf',sep='')
pdf(outpdf,height=4,width=4)
p <- ggplot(data=data, aes(x=p1,y=p2))+geom_point()+geom_smooth(color="red",method="loess",se=F)
if (expr == 'count'){
    p <- p+theme_bw()+labs(x=paste("Log2(count+0.25) of ",colnames(data)[1],sep=''), y=paste("Log2(count+0.25) of ",colnames(data)[2],sep=''))+theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
} else if (expr == 'fpkm'){
    p <- p+theme_bw()+labs(x=paste("Log2(FPKM+0.25) of ",colnames(data)[1],sep=''), y=paste("Log2(FPKM+0.25) of ",colnames(data)[2],sep=''))+theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
} else {
    print("'expr' should be 'count/fpkm'!")
}
print(p)
dev.off()

colnames(data)[c(1,3)]
cor.test(data$p1,data$p3)
corh=cor.test(data$p1,data$p3)
outcor=out_cor(corh)
outtxt=paste(colnames(data)[1],'_',colnames(data)[3],'_',nfiltern,'_cor.txt',sep='')
write(outcor,file=outtxt)

outpdf=paste(colnames(data)[1],'_',colnames(data)[3],'_',nfiltern,'_cor.pdf',sep='')
pdf(outpdf,height=4,width=4)
p <- ggplot(data=data, aes(x=p1,y=p3))+geom_point()+geom_smooth(color="red",method="loess",se=F)
if (expr == 'count'){
    p <- p+theme_bw()+labs(x=paste("Log2(count+0.25) of ",colnames(data)[1],sep=''), y=paste("Log2(count+0.25) of ",colnames(data)[3],sep=''))+theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
} else if (expr == 'fpkm'){
    p <- p+theme_bw()+labs(x=paste("Log2(FPKM+0.25) of ",colnames(data)[1],sep=''), y=paste("Log2(FPKM+0.25) of ",colnames(data)[3],sep=''))+theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
} else {
    print("'expr' should be 'count/fpkm'!")
}
print(p)
dev.off()

colnames(data)[2:3]
cor.test(data$p2,data$p3)
corh=cor.test(data$p2,data$p3)
outcor=out_cor(corh)
outtxt=paste(colnames(data)[2],'_',colnames(data)[3],'_',nfiltern,'_cor.txt',sep='')
write(outcor,file=outtxt)

outpdf=paste(colnames(data)[2],'_',colnames(data)[3],'_',nfiltern,'_cor.pdf',sep='')
pdf(outpdf,height=4,width=4)
p <- ggplot(data=data, aes(x=p2,y=p3))+geom_point()+geom_smooth(color="red",method="loess",se=F)
if (expr == 'count'){
    p <- p+theme_bw()+labs(x=paste("Log2(count+0.25) of ",colnames(data)[2],sep=''), y=paste("Log2(count+0.25) of ",colnames(data)[3],sep=''))+theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
} else if (expr == 'fpkm'){
    p <- p+theme_bw()+labs(x=paste("Log2(FPKM+0.25) of ",colnames(data)[2],sep=''), y=paste("Log2(FPKM+0.25) of ",colnames(data)[3],sep=''))+theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
} else {
    print("'expr' should be 'count/fpkm'!")
}
print(p)
dev.off()

