
import tensorflow as tf
import matplotlib.pyplot as plt
# 將張量裡的數值全部填上隨機值
# 標準差在機率統計中最常使用作為測量一組數值的離散程度之用,
# 標準差=隨機值 – 平均值


random_normal = tf.random_normal( [100] , 0 , 1)
with tf.Session() as sess:
    print( random_normal.eval() )
    plt.hist( random_normal.eval() )
    plt.show()
