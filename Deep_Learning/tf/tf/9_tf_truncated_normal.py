import tensorflow as tf
import matplotlib.pyplot as plt

# 將張量裡的數值全部填上隨機值，但不超過2倍標準差( 標準差=隨機值 – 平均值)

n = 5000000
A = tf.truncated_normal([n,])
B = tf.random_normal([n,])
with tf.Session() as sess:
    a, b = sess.run([A, B])
    plt.hist(b, 100, (-5, 5));
    plt.show()
    plt.hist(a, 100, (-5, 5));
    plt.show()
