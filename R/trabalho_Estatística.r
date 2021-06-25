Comandos no R:
-
Ir para o diretório/pasta onde os dados estão selecionados
x=read.table(file.choose())
dadosA.txt
y=read.table(file.choose())
dadosB.txt
x = x$V1
y = y$V1
summary(x)
summary(y)
var(x)
var(y)
boxplot(x,main=”Boxplot do conjunto A”,xlab=”Tempo de permanência no fundo
[dias]”,col=’deepskyblue’,horizontal=T)
boxplot(y,main=’Boxplot do conjunto B’,xlab=’Retorno do investimento
[%]’,col=’red1’,horizontal=T)
hist(x,main=“Histograma - Dados A”,col=’deepskyblue’,xlab=“Tempo
[dias]”,ylab=“frequência”,nclass=10)
hist(y,main=“Histograma - Dados B”,col=’red1’,xlab=“Retorno do investimento
[%]”,ylab=“frequˆencia”,nclass=10)
plot(x,y, xlab=“Tempo [dias]”, ylab=“Retorno do Investimento [%]”,main=“Retorno do
investimento em função do tempo de permanência no fundo”,cex=0.5,lwd=3,col=”orange”)
z = cos(cos(x*3.1415/180))
sd(z)
fit=lm(y ∼ z)
summary(fit)
plot(z,y, xlab="z = cos(cos(x.3,1415/180))", ylab="Retorno do Investimento
[%]",main="Correlação adaptada - y(z) = cos(cos(x.k)).a + b",cex=0.5,lwd=3,col="orange")
-Equação obtida: y(x) = 24.7248 -34.9230.cos(cos(x.3,1415/180)) [R2 = 0.9563]
num=length(y[y>=0])
den=length(y)
P = num/den
- Para cálculo de probabilidade de 40 e 50 % das pessoas terem rentabilidade positiva
u = 1-pbinom(40, 100, 0.408)
u = 1-pbinom(50, 100, 0.408)
t.test(dados,mu=10,alt=“less”)
prop.test(204,500,p=0.45,alt=“less”)
ks.test(x,pnorm,mean(x),sd(x))
