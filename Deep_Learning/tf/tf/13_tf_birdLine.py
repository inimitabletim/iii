# 匯入必要工具包
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# ※準備資料階段

#鳥王隨機產生100個棲息座標x_data
x_data = np.random.rand(100).astype(np.float32)
# 鳥王的指令
y_data = x_data * 8
#然而飛鳥棲息位置，會與實際有所偏移，偏移值noise_data
noise_data = np.random.normal(0.0, 0.5, 100).astype(np.float32)
# 統計100點實際飛鳥棲息的偏移值
plt.hist(noise_data)
plt.show()

# 眾鳥們實際100次飛行的落點(把偏移值也考慮進去)
y_data = x_data * 8 + noise_data
# 最後畫出飛鳥實際棲息的分布圖
plt.plot(x_data, y_data, 'o', label='data: y_data=x_data*8 + noise_data')
plt.legend()
plt.show()

# ※設定演算法階段

# 初始化權重值a ：我們隨機產生一個-1到1之間的值
a = tf.Variable( tf.random_uniform( [1], -1.0, 1.0 ) )
# 初始化權重值b ：我們產生一個0值
b = tf.Variable( tf.zeros( [1] ) )
# 機器要學習的特徵模型
y = a * x_data + b

# ※設定演算法階段

# 損失函數 lost
lost = tf.reduce_mean( tf.square ( y - y_data ) )
#優化方法: 梯度下降法
optimizer = tf.train.GradientDescentOptimizer ( learning_rate = 0.5 )
#找出最小的損失
train = optimizer.minimize ( lost )

# ※執行階段

# 初始化所有變數
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    loss_list = []
    for step in range(200): # 訓練100次
        sess.run(train)
        # 將每次訓練的誤差值收集起來
        loss_list.append(sess.run(lost))

        if step % 10 == 0:
            # 每10次把當時的權重值a,b印出來
            print(step, sess.run(a), sess.run(b))

            # 每10次把迴歸線畫出來
            plt.plot(x_data, sess.run(a)* x_data+ sess.run(b),label='model train step={}'.format(step))

            # 把原始的飛鳥棲息分布圖畫出來
            plt.plot(x_data, y_data, 'o', label='data: y_data=x_data*8 + noise_data')
            plt.legend()
            plt.show()

# 將誤差值畫出來
plt.plot(loss_list, lw=2)
plt.show()