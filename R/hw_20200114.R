getwd()
setwd("e:/R/riii/data")
match = read.table("match.txt" ,header = FALSE, sep="|")                                                                                                   
mat = matrix(0,nrow=5,ncol=5)
#colnames(mat) = c('A','B','C','D','E')
colnames(mat) = c(levels(match$V1))
rownames(mat) = c(levels(match$V2))
for (i in (rownames(mat))) {
  for (j in (colnames(mat))) {
    if(i>j)
    {mat[i,j]=match[match$V1==i & match$V2==j, 3]}
    else if(i<j)
    {mat[i,j]=match[match$V1==i & match$V2==j, 3]}    
    else
    {mat[i,j]=-1}
    
  }
  
}
mat


# for (i in rownames(mat)) {
#   for (j in colnames(mat)) {
#     if(i==j)
#     {mat[i,j]=-1}
#     else
#     {mat[i,j]=match[match$V1==i & match$V2==j, 3]}
#     
#   }
#   
# }