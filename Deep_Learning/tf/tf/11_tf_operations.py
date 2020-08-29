import tensorflow as tf
import matplotlib.pyplot as plt

a = tf.constant(8)
b = tf.constant(5)
tf_add = a + b
tf_subtract = a-b
tf_multiply = a * b
tf_divide = a / b
tf_pow = a**b
tf_mod = a % b
tf_div = a // b
with tf.Session() as sess:
    print(sess.run
    (tf_add))
    print(sess.run
    (tf_subtract))
    print(sess.run
    (tf_multiply))
    print(sess.run
    (tf_divide))
    print(sess.run
    (tf_pow))
    print(sess.run
    (tf_mod))
    print(sess.run
    (tf_div))
