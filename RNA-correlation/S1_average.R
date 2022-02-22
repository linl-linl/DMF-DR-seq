args=commandArgs(T)

file=args[1]
m=strsplit(file,split='_')[[1]]
col=paste(m[1],m[2],sep='_')
expr=strsplit(m[3],split='.txt')[[1]][1]
outname=paste(m[1],m[2],expr,'average.txt',sep='_')
data=read.table(file,header=T,row.names=1,sep='\t')
data$average=rowMeans(data)
out=data.frame(S_Bulk=data$average)
colnames(out)=col
rownames(out)=rownames(data)
write.table(out,outname,row.names=T,col.names=T,sep='\t')

