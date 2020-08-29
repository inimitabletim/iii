import tensorflow as tf

# ：給一個數值範圍內的上下界，並且設定要產生幾個元素, 裡面的元素以等差方式增加
linspace = tf.linspace( 1.0, 5.0 , 3)
with tf.Session() as sess:
    print(sess.run(linspace))