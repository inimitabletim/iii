import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
# ※資料準備中

x = tf.placeholder(tf.float32, shape=[None, 784])
Y = tf.placeholder(tf.float32, shape=[None, 10])
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
#模型公式
y_ = tf.matmul(x, W) + b

# ※設定演算法與超參數

lr = 0.5
batch_size = 2000
epochs = 1000
epoch_list=[]
accuracy_list=[]
loss_list=[]
#設定成本函數
loss = tf.reduce_mean( tf.nn.softmax_cross_entropy_with_logits(labels=Y, logits=y_))
train = tf.train.GradientDescentOptimizer(lr).minimize(loss)
#計算正確率
correct_prediction = tf.equal(tf.argmax(y_,1), tf.argmax(Y,1))
cp = tf.cast(correct_prediction, tf.float32)
accuracy = tf.reduce_mean(cp)

# ※設定模型存放位置

model_path = "/tmp/model.ckpt"
saver = tf.train.Saver()

# ※執行運算

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(epochs + 1):
        batch_x, batch_y = mnist.train.next_batch(batch_size) # 每次訓練會隨機輸入一個batch_size的數量做訓練
        _, accuracy_, loss_, cp_ = sess.run([train, accuracy, loss, cp], feed_dict={x: batch_x, Y: batch_y})
        epoch_list.append(epoch)
        accuracy_list.append(accuracy_)
        loss_list.append(loss_)
    if epoch % 100 == 0:
        # print(“cp_len={} cp={}”.format(len(cp_),cp_)) #查看一個訓練批次的cp值
        print("accuracy={} loss={} epochs={}".format(accuracy_, loss_,epoch))

        plt.subplot(1, 2, 1)
        plt.plot(epoch_list, accuracy_list, lw=2)
        plt.xlabel("epoch")
        plt.ylabel("accuracy ")
        plt.title("train set: lr={} batch_size={} epochs={}".format(lr, batch_size, epochs))
        plt.subplot(1, 2, 2)

        plt.plot(epoch_list, loss_list, lw=2)
        plt.xlabel("epoch")
        plt.ylabel("loss ")
        plt.title("train set: lr={} batch_size={} epochs={}".format(lr, batch_size, epochs))
        plt.show()

print("訓練結束!!")