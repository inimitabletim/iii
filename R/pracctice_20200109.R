#2019-01-09
test.data = read.table('match.txt' ,header = T,sep = "|")
class("2010-01-09")
as.Date("2010-01-09")
class(as.Date("2010-01-09"))
as.Date("2010-01-09") < "2020-01-01"
#年 %y 月 %m 日 $d  時 %h,%H 分 %M 秒 %S

install.packages("readr")
library(readr)
install.packages("tidyverse")
library(tidyverse)


for (i in 1:9) {
  for (j in 1:9) {
    print(paste(i ,'*', j,'=',i*j),)
  }
}


