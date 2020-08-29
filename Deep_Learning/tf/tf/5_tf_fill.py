import tensorflow as tf

# 建構內容數值皆為 特定值 的常數張量
fill = tf.fill( [1,3] ,5 )
with tf.Session() as sess:
    print(sess.run(fill))