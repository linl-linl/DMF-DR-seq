library("ggplot2")

zscore1=function(x){
 return(scale(x,center=1)) 
}
zscore2=function(x){
 return(scale(x,center=2)) 
}

data<-read.table('Merge',header=T)
dna=data[,c(1,3,5,7,9,11,13,15,17)]
rna=data[,c(2,4,6,8,10,12,14,16,18)]

rna1=rna[1:3]
dna1=dna[1:3]
rna1=apply(rna1,2,zscore1)
dna1=apply(dna1,2,zscore2)
dna1[dna1<0.25]=0.25
dna1=log(dna1)/log(2)
round(cor(dna1,rna1),2)
data1<-cbind(dna1,rna1)
data1<-data.frame(data1)

rna2=rna[4:6]
dna2=dna[4:6]
rna2=apply(rna2,2,zscore1)
dna2=apply(dna2,2,zscore2)
dna2[dna2<0.25]=0.25
dna2=log(dna2)/log(2)
round(cor(dna2,rna2),2)
data2<-cbind(dna2,rna2)
data2<-data.frame(data2)

rna3=rna[7:9]
dna3=dna[7:9]
rna3=apply(rna3,2,zscore1)
dna3=apply(dna3,2,zscore2)
dna3[dna3<0.25]=0.25
dna3=log(dna3)/log(2)
round(cor(dna3,rna3),2)
data3<-cbind(dna3,rna3)
data3<-data.frame(data3)

# H_BulkD
# cor.test(data1$H_BulkD,data1$H_BulkR)
pdf('H_BulkD+H_BulkR_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_BulkD,y=H_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkD", y="H_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data1$H_BulkD,data1$H_FR)
pdf('H_BulkD+H_FR_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_BulkD,y=H_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkD", y="H_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data1$H_BulkD,data1$H_WR)
pdf('H_BulkD+H_WR_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_BulkD,y=H_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkD", y="H_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# H_WD
# cor.test(data1$H_WD,data1$H_BulkR)
pdf('H_WD+H_BulkR_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_WD,y=H_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_WD", y="H_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data1$H_WD,data1$H_FR)
pdf('H_WD+H_FR_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_WD,y=H_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_WD", y="H_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data1$H_WD,data1$H_WR)
pdf('H_WD+H_WR_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_WD,y=H_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_WD", y="H_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# H_FD
# cor.test(data1$H_FD,data1$H_BulkR)
pdf('H_FD+H_BulkR_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_FD,y=H_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_FD", y="H_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data1$H_FD,data1$H_FR)
pdf('H_FD+H_FR_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_FD,y=H_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_FD", y="H_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data1$H_FD,data1$H_WR)
pdf('H_FD+H_WR_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_FD,y=H_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_FD", y="H_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# M_BulkD
# cor.test(data2$M_BulkD,data2$M_BulkR)
pdf('M_BulkD+M_BulkR_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_BulkD,y=M_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkD", y="M_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data2$M_BulkD,data2$M_FR)
pdf('M_BulkD+M_FR_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_BulkD,y=M_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkD", y="M_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data2$M_BulkD,data2$M_WR)
pdf('M_BulkD+M_WR_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_BulkD,y=M_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkD", y="M_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# M_WD
# cor.test(data2$M_WD,data2$M_BulkR)
pdf('M_WD+M_BulkR_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_WD,y=M_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_WD", y="M_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data2$M_WD,data2$M_FR)
pdf('M_WD+M_FR_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_WD,y=M_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_WD", y="M_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data2$M_WD,data2$M_WR)
pdf('M_WD+M_WR_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_WD,y=M_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_WD", y="M_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# M_FD
# cor.test(data2$M_FD,data2$M_BulkR)
pdf('M_FD+M_BulkR_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_FD,y=M_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_FD", y="M_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data2$M_FD,data2$M_FR)
pdf('M_FD+M_FR_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_FD,y=M_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_FD", y="M_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data2$M_FD,data2$M_WR)
pdf('M_FD+M_WR_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_FD,y=M_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_FD", y="M_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# S_BulkD
# cor.test(data3$S_BulkD,data3$S_BulkR)
pdf('S_BulkD+S_BulkR_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_BulkD,y=S_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkD", y="S_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data3$S_BulkD,data3$S_FR)
pdf('S_BulkD+S_FR_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_BulkD,y=S_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkD", y="S_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data3$S_BulkD,data3$S_WR)
pdf('S_BulkD+S_WR_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_BulkD,y=S_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkD", y="S_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# S_WD
# cor.test(data3$S_WD,data3$S_BulkR)
pdf('S_WD+S_BulkR_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_WD,y=S_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_WD", y="S_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data3$S_WD,data3$S_FR)
pdf('S_WD+S_FR_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_WD,y=S_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_WD", y="S_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data3$S_WD,data3$S_WR)
pdf('S_WD+S_WR_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_WD,y=S_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_WD", y="S_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# S_FD
# cor.test(data3$S_FD,data3$S_BulkR)
pdf('S_FD+S_BulkR_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_FD,y=S_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_FD", y="S_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data3$S_FD,data3$S_FR)
pdf('S_FD+S_FR_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_FD,y=S_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_FD", y="S_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# cor.test(data3$S_FD,data3$S_WR)
pdf('S_FD+S_WR_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_FD,y=S_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_FD", y="S_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

