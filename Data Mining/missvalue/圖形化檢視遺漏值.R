install.packages("VIM") 
library(VIM)
aggr_plot <- aggr(data, col = c('navyblue', 'red'), numbers=TRUE, sortVars=TRUE,
                    labels=names(data), cex.axis=.7, gap=3,
                    ylab=c("Histogram of missing data", "Pattern"))
