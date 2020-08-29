# p109 重新編碼
data(cars)
str(cars)
summary(cars)

# p110
# 將速度分成3類,
# 第一類 speed<12 ; 第二類 speed <15 ; 第三類 speed >= 15
cars$speed
x1 = cars$speed
new_cars_band = 1*(x1<12) + 2*(x1>=12 & x1<15) + 3*(x1>=15)

new_cars_band
# 將數字標籤轉成文字
label = c('慢','中','快')
new_cars_band = label[new_cars_band]
new_cars_band

# 再將速度標籤轉碼，變成車種標籤
# '慢' , '中' 轉成 '一般轎車' ; '快' 轉成'跑車'
# 使用 %in%
car_categ = c('一般轎車','跑車')
new_cars_band_1 = 1*(new_cars_band %in% c('慢','中')) + 2*(new_cars_band %in% c('快'))
new_cars_band_1 = car_categ[new_cars_band_1]
new_cars_band_1

# p111 ifelse
# 再將車種標籤轉碼
# '一般轎車'轉成 1 ; '跑車'轉成 0
new_cars_band_2 = 1*(new_cars_band_1 %in% c('一般轎車')) + 0*(new_cars_band_1 %in% c('跑車'))
# 也可使用 ifelse (條件式, 真, 假)，效果一樣
new_cars_band_2 = ifelse(new_cars_band_1 =='一般轎車', 1,0)
new_cars_band_3 = ifelse(new_cars_band %in% c('慢','中') ,'一般轎車','跑車')

# p111 within
# within就像是SQL語法中的Case When
# 將速度分成3類, 慢: speed<12 ; 中: speed <15 ; 快 speed >= 15
new_cars <- cars
new_cars <- within(new_cars,
                     {
                       speed_level <- NA #一定要指定一個值
                       speed_level[cars$speed<12] <- "慢"
                       speed_level[cars$speed>=12 & cars$speed<15] <- "中"
                       speed_level[cars$speed>=15] <- "快"
                     }
)
head(new_cars,5)

