# new_data = data[complete.cases(data),]
# summary(new_data)

new_data1 <- data

new_data1.mean_col_1 <- mean(new_data1[, 1], na.rm = T)
new_data1.mean_col_2 <- mean(new_data1[, 2], na.rm = T)
new_data1.mean_col_3 <- mean(new_data1[, 3], na.rm = T)
new_data1.mean_col_4 <- mean(new_data1[, 4], na.rm = T)

na.rows1 <- is.na(new_data1[, 1])
na.rows2 <- is.na(new_data1[, 2])
na.rows3 <- is.na(new_data1[, 3])
na.rows4 <- is.na(new_data1[, 4])

new_data1[na.rows1,1] <- new_data1.mean_col_1
new_data1[na.rows2,2] <- new_data1.mean_col_2
new_data1[na.rows3,3] <- new_data1.mean_col_3
new_data1[na.rows4,4] <- new_data1.mean_col_4
new_data1
