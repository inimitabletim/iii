# 將模型保存在指定的位置
save_path = saver.save(sess, model_path)
print("模型保存在: {}".format(save_path))
# 評估模型
# 在測試集上的準確率
accu_test = sess.run(accuracy, feed_dict={x: mnist.test.images,
y: mnist.test.labels})
print("Test Accuracy:", accu_test)
# 在驗證集上的準確率
accu_validation = sess.run(accuracy, feed_dict={x: mnist.validation.images, y:
mnist.validation.labels})
print("valid Accuracy:", accu_validation)
# 訓練集上的準確率
accu_train = sess.run(accuracy, feed_dict={x: mnist.train.images,
y: mnist.train.labels})
print("train Accuracy:", accu_train)

# 載入保存的模型
with tf.Session() as sess:
sess.run(init)
# 載入保存的模型
saver.restore(sess, model_path)
# 評估在測試集上的準確率
print("Testing Accuracy:", sess.run(accuracy, feed_dict={x: mnist.test.images, Y:
mnist.test.labels}))
# 使用訓練好的模型來預測測試集裡圖像的數字
prediction_result = sess.run(tf.argmax(y_, 1), feed_dict={x: mnist.test.images})
# 畫出測試集的第一張圖像
matrix = data_to_matrix(mnist.test.images[0])
plt.figure()
plt.imshow(matrix)
plt.show()
# 第一張圖像的預測結果
print(prediction_result[0:1])
