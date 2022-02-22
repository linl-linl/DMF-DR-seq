library("ggplot2")
data<-read.table('Merge',header=T)
#data$H_BulkD=log(data$H_BulkD+0.001)/log(2)
#data$H_WD=log(data$H_WD+0.001)/log(2)
#data$H_FD=log(data$H_FD+0.001)/log(2)
#data$M_BulkD=log(data$M_BulkD+0.001)/log(2)
#data$M_WD=log(data$M_WD+0.001)/log(2)
#data$M_FD=log(data$M_FD+0.001)/log(2)
#data$S_BulkD=log(data$S_BulkD+0.001)/log(2)
#data$S_WD=log(data$S_WD+0.001)/log(2)
#data$S_FD=log(data$S_FD+0.001)/log(2)

# H_BulkD
cor.test(data$H_BulkD,data$H_BulkR)
pdf('H_BulkD+H_BulkR.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_BulkD,y=H_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkD", y="H_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_BulkD,data$H_FR)
pdf('H_BulkD+H_FR.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_BulkD,y=H_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkD", y="H_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_BulkD,data$H_WR)
pdf('H_BulkD+H_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_BulkD,y=H_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_BulkD", y="H_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# H_WD
cor.test(data$H_WD,data$H_BulkR)
pdf('H_WD+H_BulkR.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_WD,y=H_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_WD", y="H_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_WD,data$H_FR)
pdf('H_WD+H_FR.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_WD,y=H_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_WD", y="H_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_WD,data$H_WR)
pdf('H_WD+H_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_WD,y=H_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_WD", y="H_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# H_FD
cor.test(data$H_FD,data$H_BulkR)
pdf('H_FD+H_BulkR.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_FD,y=H_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_FD", y="H_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_FD,data$H_FR)
pdf('H_FD+H_FR.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_FD,y=H_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_FD", y="H_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$H_FD,data$H_WR)
pdf('H_FD+H_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=H_FD,y=H_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="H_FD", y="H_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# M_BulkD
cor.test(data$M_BulkD,data$M_BulkR)
pdf('M_BulkD+M_BulkR.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_BulkD,y=M_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkD", y="M_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_BulkD,data$M_FR)
pdf('M_BulkD+M_FR.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_BulkD,y=M_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkD", y="M_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_BulkD,data$M_WR)
pdf('M_BulkD+M_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_BulkD,y=M_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_BulkD", y="M_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# M_WD
cor.test(data$M_WD,data$M_BulkR)
pdf('M_WD+M_BulkR.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_WD,y=M_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_WD", y="M_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_WD,data$M_FR)
pdf('M_WD+M_FR.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_WD,y=M_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_WD", y="M_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_WD,data$M_WR)
pdf('M_WD+M_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_WD,y=M_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_WD", y="M_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# M_FD
cor.test(data$M_FD,data$M_BulkR)
pdf('M_FD+M_BulkR.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_FD,y=M_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_FD", y="M_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_FD,data$M_FR)
pdf('M_FD+M_FR.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_FD,y=M_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_FD", y="M_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$M_FD,data$M_WR)
pdf('M_FD+M_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=M_FD,y=M_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="M_FD", y="M_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# S_BulkD
cor.test(data$S_BulkD,data$S_BulkR)
pdf('S_BulkD+S_BulkR.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_BulkD,y=S_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkD", y="S_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_BulkD,data$S_FR)
pdf('S_BulkD+S_FR.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_BulkD,y=S_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkD", y="S_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_BulkD,data$S_WR)
pdf('S_BulkD+S_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_BulkD,y=S_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_BulkD", y="S_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# S_WD
cor.test(data$S_WD,data$S_BulkR)
pdf('S_WD+S_BulkR.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_WD,y=S_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_WD", y="S_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_WD,data$S_FR)
pdf('S_WD+S_FR.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_WD,y=S_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_WD", y="S_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_WD,data$S_WR)
pdf('S_WD+S_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_WD,y=S_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_WD", y="S_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

# S_FD
cor.test(data$S_FD,data$S_BulkR)
pdf('S_FD+S_BulkR.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_FD,y=S_BulkR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_FD", y="S_BulkR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_FD,data$S_FR)
pdf('S_FD+S_FR.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_FD,y=S_FR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_FD", y="S_FR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

cor.test(data$S_FD,data$S_WR)
pdf('S_FD+S_WR.pdf',width=5,height=5)
ggplot(data=data, aes(x=S_FD,y=S_WR))+geom_point()+
  geom_smooth(color="red",method="lm",se=F)+theme_bw()+labs(x="S_FD", y="S_WR")+
  theme(panel.border=element_blank(),panel.grid.major=element_blank(),panel.grid.minor=element_blank(),axis.line=element_line(color="black"))
dev.off()

