library("ggplot2")

data<-read.table('../Merge',header=T)

dna=data[,c(1,3,5,7,9,11,13,15,17)]
rna=data[,c(2,4,6,8,10,12,14,16,18)]
rna1=rna[1:3]
dna1=dna[1:3]
rna2=rna[4:6]
dna2=dna[4:6]
rna3=rna[7:9]
dna3=dna[7:9]
round(cor(dna1,dna1),2)
round(cor(rna1,rna1),2)
round(cor(dna2,dna2),2)
round(cor(rna2,rna2),2)
round(cor(dna3,dna3),2)
round(cor(rna3,rna3),2)

# H_D
cor.test(data$H_BulkD,data$H_FD)
pdf('H_BulkD+H_FD.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_BulkD,y=H_FD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkD", y="H_FD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_BulkD,data$H_WD)
pdf('H_BulkD+H_WD.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_BulkD,y=H_WD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkD", y="H_WD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_FD,data$H_WD)
pdf('H_FD+H_WD.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_FD,y=H_WD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_FD", y="H_WD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# M_D
cor.test(data$M_BulkD,data$M_FD)
pdf('M_BulkD+M_FD.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_BulkD,y=M_FD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkD", y="M_FD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_BulkD,data$M_WD)
pdf('M_BulkD+M_WD.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_BulkD,y=M_WD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkD", y="M_WD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_FD,data$M_WD)
pdf('M_FD+M_WD.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_FD,y=M_WD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_FD", y="M_WD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# S_D
cor.test(data$S_BulkD,data$S_FD)
pdf('S_BulkD+S_FD.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_BulkD,y=S_FD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkD", y="S_FD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_BulkD,data$S_WD)
pdf('S_BulkD+S_WD.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_BulkD,y=S_WD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkD", y="S_WD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_FD,data$S_WD)
pdf('S_FD+S_WD.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_FD,y=S_WD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_FD", y="S_WD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()


# H_R
cor.test(data$H_BulkR,data$H_FR)
pdf('H_BulkR+H_FR.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_BulkR,y=H_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkR", y="H_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_BulkR,data$H_WR)
pdf('H_BulkR+H_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_BulkR,y=H_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkR", y="H_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_FR,data$H_WR)
pdf('H_FR+H_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_FR,y=H_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_FR", y="H_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# M_R
cor.test(data$M_BulkR,data$M_FR)
pdf('M_BulkR+M_FR.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_BulkR,y=M_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkR", y="M_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_BulkR,data$M_WR)
pdf('M_BulkR+M_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_BulkR,y=M_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkR", y="M_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_FR,data$M_WR)
pdf('M_FR+M_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_FR,y=M_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_FR", y="M_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# S_R
cor.test(data$S_BulkR,data$S_FR)
pdf('S_BulkR+S_FR.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_BulkR,y=S_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkR", y="S_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_BulkR,data$S_WR)
pdf('S_BulkR+S_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_BulkR,y=S_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkR", y="S_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_FR,data$S_WR)
pdf('S_FR+S_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_FR,y=S_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_FR", y="S_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()




zscore1=function(x){
 return(scale(x,center=1)) 
}
zscore2=function(x){
 return(scale(x,center=2)) 
}

dna=data[,c(1,3,5,7,9,11,13,15,17)]
rna=data[,c(2,4,6,8,10,12,14,16,18)]

rna1=rna[1:3]
dna1=dna[1:3]
rna1=apply(rna1,2,zscore1)
dna1=apply(dna1,2,zscore2)
dna1[dna1<0.25]=0.25
dna1=log(dna1)/log(2)
round(cor(dna1,dna1),2)
round(cor(rna1,rna1),2)
data1<-cbind(dna1,rna1)
data1<-data.frame(data1)

rna2=rna[4:6]
dna2=dna[4:6]
rna2=apply(rna2,2,zscore1)
dna2=apply(dna2,2,zscore2)
dna2[dna2<0.25]=0.25
dna2=log(dna2)/log(2)
round(cor(dna2,dna2),2)
round(cor(rna2,rna2),2)
data2<-cbind(dna2,rna2)
data2<-data.frame(data2)

rna3=rna[7:9]
dna3=dna[7:9]
rna3=apply(rna3,2,zscore1)
dna3=apply(dna3,2,zscore2)
dna3[dna3<0.25]=0.25
dna3=log(dna3)/log(2)
round(cor(dna3,dna3),2)
round(cor(rna3,rna3),2)
data3<-cbind(dna3,rna3)
data3<-data.frame(data3)


# H_D
cor.test(data$H_BulkD,data$H_FD)
pdf('H_BulkD+H_FD_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_BulkD,y=H_FD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkD", y="H_FD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_BulkD,data$H_WD)
pdf('H_BulkD+H_WD_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_BulkD,y=H_WD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkD", y="H_WD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_FD,data$H_WD)
pdf('H_FD+H_WD_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_FD,y=H_WD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_FD", y="H_WD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# M_D
cor.test(data$M_BulkD,data$M_FD)
pdf('M_BulkD+M_FD_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_BulkD,y=M_FD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkD", y="M_FD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_BulkD,data$M_WD)
pdf('M_BulkD+M_WD_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_BulkD,y=M_WD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkD", y="M_WD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_FD,data$M_WD)
pdf('M_FD+M_WD_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_FD,y=M_WD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_FD", y="M_WD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# S_D
cor.test(data$S_BulkD,data$S_FD)
pdf('S_BulkD+S_FD_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_BulkD,y=S_FD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkD", y="S_FD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_BulkD,data$S_WD)
pdf('S_BulkD+S_WD_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_BulkD,y=S_WD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkD", y="S_WD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_FD,data$S_WD)
pdf('S_FD+S_WD_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_FD,y=S_WD))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_FD", y="S_WD")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()


# H_R
cor.test(data$H_BulkR,data$H_FR)
pdf('H_BulkR+H_FR_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_BulkR,y=H_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkR", y="H_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_BulkR,data$H_WR)
pdf('H_BulkR+H_WR_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_BulkR,y=H_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkR", y="H_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_FR,data$H_WR)
pdf('H_FR+H_WR_adj.pdf',width=5,height=5)
ggplot(data=data1, aes(x=H_FR,y=H_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_FR", y="H_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# M_R
cor.test(data$M_BulkR,data$M_FR)
pdf('M_BulkR+M_FR_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_BulkR,y=M_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkR", y="M_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_BulkR,data$M_WR)
pdf('M_BulkR+M_WR_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_BulkR,y=M_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkR", y="M_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_FR,data$M_WR)
pdf('M_FR+M_WR_adj.pdf',width=5,height=5)
ggplot(data=data2, aes(x=M_FR,y=M_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_FR", y="M_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# S_R
cor.test(data$S_BulkR,data$S_FR)
pdf('S_BulkR+S_FR_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_BulkR,y=S_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkR", y="S_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_BulkR,data$S_WR)
pdf('S_BulkR+S_WR_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_BulkR,y=S_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkR", y="S_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_FR,data$S_WR)
pdf('S_FR+S_WR_adj.pdf',width=5,height=5)
ggplot(data=data3, aes(x=S_FR,y=S_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_FR", y="S_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

merge<-cbind(data1,data2,data3)
write.table(merge,'Merge_adj',row.names=F,col.names=T,sep='\t')

