import keras
#匯入MNIST資料
from keras.datasets import mnist
#使用Sequential模型
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D
from keras.callbacks import EarlyStopping, CSVLogger
import matplotlib.pyplot as plt
# 每一批次讀入128張資料
batch_size = 200
# 數字為0~9所以共10個類別
num_classes = 10
# 使用反向傳播法進行訓練，總共訓練20次
epochs = 10

# 讀取MNIST資料為Tuple形式, x_train為影像資料, y_train為標籤資料
# X shape (60,000 28x28), y shape (10,000, )
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 將輸入的資料正規劃 #28x28x1一通道的灰階圖
x_train = x_train.reshape(60000,28,28,1).astype('float32')
x_test = x_test.reshape(10000,28,28,1).astype('float32')
# 輸入的x變成60,000*784的數據，然後除以255進行標準化，每個像素都是在0到255之間
# 的(顏色階數從0~255)，標準化之後就變成了0到1之間。
x_train /= 255
x_test /= 255
#把y變成了one-hot的形式
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)
# 印出形狀
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

model = Sequential()
#第一層
model.add(Conv2D(filters=10,
kernel_size=(3,3),
padding='same',
input_shape=(28,28,1),
activation='relu'
))
#第二層
model.add(MaxPooling2D(pool_size=(2,2)))

#第三層
model.add(Conv2D(filters=20,
kernel_size=(3,3),
padding='same',
activation='relu'))
#第四層
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.2))
#第五層
model.add(Flatten())
#第六層
model.add(Dense(256,activation='relu'))
model.add(Dropout(0.2))
#第七層
model.add(Dense(10,activation='softmax'))
# 顯示出模型摘要
model.summary()

# 損失函數用交叉熵,
#優化器用RMSprop
#metrics，裡面可以放入accuracy
model.compile(loss='categorical_crossentropy',
optimizer='adam',
metrics=['accuracy'])
#將epoch的訓練結果保存在csv文件中
logger = CSVLogger('training.log')
#當監測值val_loss不再改善時，如發現損失沒有下降，則經過3個epoch後停止訓練。
estop = EarlyStopping(monitor='val_loss', patience=3)

# validation_split：0~1之間的浮點數，用來指定訓練集的比例作為驗證集數據。
hist = model.fit(x_train, y_train,
batch_size=batch_size,
epochs=epochs,
verbose=2,
validation_split=0.2,
callbacks=[logger,estop])
# 進行學習評估
score = model.evaluate(x_test, y_test, verbose=0)
print('test loss:', score[0])
print('test acc:', score[1])

# 顯示acc學習結果
accuracy = hist.history['acc']
val_accuracy = hist.history["val_acc"]
plt.plot(range(len(accuracy)), accuracy, marker=".", label="accuracy(training data)")
plt.plot(range(len(val_accuracy)), val_accuracy, marker='.', label="val_accuracy(evaluation data)")
plt.legend(loc="best")
plt.grid()
plt.xlabel("epoch")
plt.ylabel("accuracy")
plt.show()
# 顯示loss學習結果
loss = hist.history['loss']
val_loss = hist.history['val_loss']
plt.plot(range(len(loss)), loss, marker='.', label='loss(training data)')
plt.plot(range(len(val_loss)), val_loss, marker='.', label='val_loss(evaluation data)')
plt.legend(loc='best')
plt.grid()
plt.xlabel('epoch')
plt.ylabel('loss')
plt.show()
# 存儲模型與權重
model.save('model_KerasMnistCNN.h5')
del model

import keras
#匯入MNIST資料
from keras.datasets import mnist
import matplotlib.pyplot as plt
from keras.models import load_model
import numpy as np
import pandas as pd
# 載入模型
model = load_model('model_KerasMnistCNN.h5')
# 顯示出模型摘要
model.summary()

# 讀取MNIST資料為Tuple形式, x_train為影像資料, y_train為標籤資料
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 保持原始數據, 之後混淆矩陣 做比較用
label_y_test = y_test
# 圖片正規劃
x_test = x_test.reshape(10000,28,28,1).astype('float32')
# 輸入的x變成60,000*784的數據，然後除以255進行標準化，每個像素都是在0
# 到255之間的(顏色階數從0~255)，標準化之後就變成了0到1之間。
x_test /= 255
#把y變成了one-hot的形式
y_test = keras.utils.to_categorical(y_test, num_classes=10)

# 驗證模型
score = model.evaluate(x_test, y_test, verbose=0)
# 輸出結果
print('Test loss:', score[0])
print('Test accuracy:', score[1])
predictions = model.predict_classes(x_test)
print(x_test.shape)
print(predictions)

# 顯示出前15個測試影像, 預測結果, 與原始答案
for i in range(15):
    plt.subplot(3, 5, i+1)
    plt.title("pred.={} label={}".format(predictions[i],np.argmax(y_test[i])))
    plt.imshow(x_test[i].reshape(28, 28))
plt.show()

print("Error prediction:")
errorList = []
for i in range(len(predictions)):
    if predictions[i] != np.argmax(y_test[i]):
        print("Image[%d] : label=%d, but prediction=%d" % (i,np.argmax(y_test[i], axis=0), predictions[i]))
        errorList.append(i)
print("-----------------------")
print("total number of error prediction is %d" % len(errorList))

print("%s\n" % pd.crosstab(label_y_test, predictions, rownames=['label'],
colnames=['predict']))



