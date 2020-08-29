install.packages("mice")
library(mice)
mice.data <- mice(data,
                  m = 3, # ���ͤT�ӿ�|�ȳQ��ɦn����ƪ�
                  maxit = 30, # �̤j�|�N��max iteration
                  method = "cart", # �ϥ�CART�M����A�i���|�ȹw��
                  seed = 188) # �O��˨C�����@��

new_data1 <- complete(mice.data, 1) #�Ĥ@�ӵ��G
new_data1
new_data2 <- complete(mice.data, 2) #�ĤG�ӵ��G
new_data2
new_data3 <- complete(mice.data, 3) #�ĤT�ӵ��G
new_data3

Training_data_set <- new_data2 #��βĤG�ӵ��G�ӷ����ҫ��V�m��ƶ�
kmeans(Training_data_set[-5] , nstart=20, centers=5) #�]���s�t��k
mice.data <- mice(data,
                  m = 3, # ���ͤT�ӿ�|�ȳQ��ɦn����ƪ�
                  maxit = 30, # �̤j�|�N��max iteration
                  method = "rf", # �ϥ��H���˪L�A�i���|�ȹw��
                  seed = 188) # �O��˨C�����@��
    