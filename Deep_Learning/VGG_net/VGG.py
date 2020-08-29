# coding: utf-8
from keras.applications.vgg16 import VGG16, preprocess_input,decode_predictions
from keras.preprocessing import image
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
from keras.preprocessing import image
import os, glob, cv2


# 載入VGG16
model = VGG16(weights="imagenet")
# 顯示出模型摘要
model.summary()

# 辨識
def predict(filename, rank):
    img = image.load_img(filename, target_size=(224, 224))
    x = image.img_to_array(img)
    print(x.shape) #(224, 224, 3)
    #在 x array的第0維新增一個資料 (np.expand_dims 用於擴充維度)
    x = np.expand_dims(x, axis=0)
    print(x.shape) #(1, 224, 224, 3)
    #預測圖片 #轉換成VGG16可以讀的格式
    preds = model.predict(preprocess_input(x))
    print(preds.shape) #(1, 1000)
    #rank 取前幾名排序
    results = decode_predictions(preds, top=rank)[0]
    return results

# 辨識
filename = "vgg16TestPic/2.jpg"
plt.figure()
im = Image.open(filename)
im_list = np.asarray(im)
plt.title("predict")
plt.axis("off")
plt.imshow(im_list)
plt.show()
results = predict(filename, 3)
for result in results:
    print(result)


# 相似矩陣的計算
# 將test2目錄內的每一張jpg取出其特徵向量，並相互比較，利用 cosine 函數計算兩張照片特徵向量的角度，
# 越接近 1，表示越相似
def cosine_similarity(featuresVector):
#與自己的轉置矩陣(T)做內積運算(dot)
    sim = featuresVector.dot(featuresVector.T)
    if not isinstance(sim, np.ndarray):
        sim = sim.toarray()
        #np.diagonal取對角線 np.sqrt取平方根
        norms = np.array([np.sqrt(np.diagonal(sim))])
        return (sim/norms/norms.T)
# 自 vgg16TestPic 目錄找出所有 JPEG 檔案
images_filename_list = []
images_data_tuple = []
for img_path in os.listdir("vgg16TestPic"):
    if img_path.endswith(".jpg"):
        img = image.load_img("vgg16TestPic/" + img_path, target_size=(224, 224))
        images_filename_list.append(img_path)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        if len(images_data_tuple) == 0:
            images_data_tuple = x
        else:
            images_data_tuple = np.concatenate((images_data_tuple, x))

images_data_tuple = preprocess_input(images_data_tuple)
# include_top=False，表示只計算出特徵, 不使用最後3層的全連接層(不用分類器)
model = VGG16(weights='imagenet', include_top=False)
# 顯示出模型摘要
model.summary()
# 預測出特徵
features = model.predict(images_data_tuple)
#計算特徵向量
featuresVector = features.reshape(len(images_filename_list), 7 * 7 * 512)
# 計算相似矩陣
sim = cosine_similarity(featuresVector)
print(sim) #印出所有照片之間的特徵值, 越接近1.0, 照片越相近
#印出目錄內的檔案
print(images_filename_list)
#測試檔案在目錄內的位置
testPicID = 2
#np.argsort 進行由小到大的排序, -sim表式將資料列反向, 最後會得到由大到小的排序
top = np.argsort(-sim[testPicID], axis=0)
rank = [images_filename_list[i] for i in top]
print('目錄內的所有照片與測試檔案 {}的相似度排序(越前面的越相似):{}'.format(images_filename_list[testPicID],rank))