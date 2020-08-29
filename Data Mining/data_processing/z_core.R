data = c(1, 2, 3, 6, 3)
scale(data,center = T,scale = F)

a <- scale(data, center=T,scale=T)
attributes(a)
