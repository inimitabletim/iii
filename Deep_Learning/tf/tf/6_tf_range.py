import tensorflow as tf

# 建構一個數值範圍內的常數張量, 裡面的元素以等差方式增加
range1 = tf.range( 5 )
range2 = tf.range( 5, delta=2 )
with tf.Session() as sess:
    print(sess.run(range1))
    print(sess.run(range2))