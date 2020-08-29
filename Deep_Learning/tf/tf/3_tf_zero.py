import tensorflow as tf
# 建構內容數值皆為 0 的常數張量
zeros = tf.zeros([1,3])
with tf.Session() as sess:
    print(sess.run(zeros))