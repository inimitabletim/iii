install.packages("mice")
library(mice)
mice.data <- mice(data,
                  m = 3, # 產生三個遺漏值被填補好的資料表
                  maxit = 30, # 最大疊代數max iteration
                  method = "cart", # 使用CART決策樹，進行遺漏值預測
                  seed = 188) # 令抽樣每次都一樣

new_data1 <- complete(mice.data, 1) #第一個結果
new_data1
new_data2 <- complete(mice.data, 2) #第二個結果
new_data2
new_data3 <- complete(mice.data, 3) #第三個結果
new_data3

Training_data_set <- new_data2 #選用第二個結果來當成模型訓練資料集
kmeans(Training_data_set[-5] , nstart=20, centers=5) #跑分群演算法
mice.data <- mice(data,
                  m = 3, # 產生三個遺漏值被填補好的資料表
                  maxit = 30, # 最大疊代數max iteration
                  method = "rf", # 使用隨機森林，進行遺漏值預測
                  seed = 188) # 令抽樣每次都一樣
    