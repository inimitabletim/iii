# --coding:utf-8--
import glob
import matplotlib.pyplot as plt
from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import numpy as np

train_dir = 'kagglecatdog/train'
test_dir = 'kagglecatdog/test'
validation_dir = 'kagglecatdog/validation'

# 讀取目錄下的圖片檔路徑, 存在files list裡
files = glob.glob("testcatdog/train/cat/*.jpg")

test_files = files[11] #隨機選擇序號第10的照片
img = image.load_img(test_files, target_size=(150, 150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)

my_test_datagen = ImageDataGenerator(
rescale=1./255, #指定將影象像素縮放到0~1之間
preprocessing_function=preprocess_input,
rotation_range=45, # 角度值，0~180，影象旋轉
width_shift_range=0.2, # 水平平移，相對總寬度的比例
height_shift_range=0.2, # 垂直平移，相對總高度的比例
shear_range=0.2, # 隨機傾斜角度
zoom_range=0.2, # 隨機縮放範圍
horizontal_flip=True,# 一半影象水平翻轉
fill_mode = 'nearest' #產生新的影像若有出現空白處，填補像素
)

i = 0
for batch in my_test_datagen.flow(x,batch_size=1):
    plt.figure(batch)
    imgplot = plt.imshow(image.array_to_img(batch[0]))
    i+=1
    if i%4==0:
        break
plt.show()
