tryCatch(
  {
    x = 2
    z = sqrt(x)
  },
  warning = function(msg) {
    message(paste("[Warning]",msg,"\n"))
    return(NULL)
  },
  error = function(msg) {
    message(paste("[Error]",msg,"\n"))
    return(NA)
  }
)
ifelse(exists("z"),z,"z does not exist!")
a= x
a