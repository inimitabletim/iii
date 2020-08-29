import tensorflow as tf

# 建構內容數值皆為 1 的常數張量
ones = tf.ones([1,3])
with tf.Session() as sess:
    print(sess.run(ones))
