# Classification
### Decision Tree - using churn data in C50 package
```{R}
#install.packages("C50")
library(C50)

data(churn)
str(churnTrain)

names(churnTrain) %in% c("state", "area_code", "account_length")
!names(churnTrain) %in% c("state", "area_code", "account_length")
#��ܫؼ��ܼ�
variable.list = !names(churnTrain) %in% c('state','area_code','account_length')
churnTrain=churnTrain[,variable.list]
churnTest=churnTest[,variable.list]

str(churnTrain)

#sample
?sample
sample(1:10)
sample(1:10, size = 5)
sample(c(0,1), size= 10, replace = T)
sample.int(20, 12) # ��ӰѼƳ��n���ơA���Ҭ���1:20����12�Ӥ����Ƽ˥�

set.seed(2)
#���Ƥ���training data �M testing data
ind<-sample(1:2, size=nrow(churnTrain), replace=T, prob=c(0.8, 0.2))
trainset=churnTrain[ind==1,]
testset=churnTrain[ind==2,]
```

### rpart
```{R}
#install.packages('rpart')
library('rpart')
#�ϥ�rpart(CART)�إߨM����ҫ�
?rpart
con = rpart.control(minsplit=20,cp=0.01)
?rpart.control
churn.rp<-rpart(churn ~., data=trainset,control = con)
#churn.rp<-rpart(churn ~ total_day_charge + international_plan, data=trainset)

churn.rp
s = summary(churn.rp)
s$cptable

#�e�X�M����
par(mfrow=c(1,1))
?plot.rpart
plot(churn.rp, uniform=TRUE,branch = 0.6, margin=0.1)
text(churn.rp, cex=0.7)

#install.packages('rpart.plot')
library('rpart.plot')
rpart.plot(churn.rp)
```