import tensorflow as tf
import matplotlib.pyplot as plt

# 將張量裡的數值全部填上隨機值，但不超過上下限

random_uniform = tf.random_uniform( [100] , 0 , )
with tf.Session() as sess:
    print(sess.run( random_uniform ))
    plt.hist(sess.run( random_uniform ))
    plt.show()