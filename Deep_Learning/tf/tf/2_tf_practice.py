import tensorflow as tf

# 匯入必要工具包
c1 = tf.constant( [0, 0, 0, 1, 0, 0, 0, 0, 0, 0] )
c2 = tf.constant( [[1, 2, 3],[4, 5, 6]] )
c3 = tf.constant( [[1, 2],[3, 4],[5, 6]] );


with tf.Session() as sess:
    print("一階張量執行後結果")
    print(sess.run((c1)))
    print("二階張量執行後結果")
    print(sess.run((c2)))
    print("二階張量執行後結果")
    print(sess.run((c3)))