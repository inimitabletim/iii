import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import  KMeans
from sklearn import  datasets

np.random.seed(5) # 設定隨機種子

iris = datasets.load_iris() # 鳶尾花資料集
X = iris.data  # 花的四種特徵
Y = iris.target  # 花的種類

est = KMeans(n_clusters=3)  # 建立KMeans模型
est.fit(X)  # 將花的特徵數據X套用到KMeans模型進行分類
labels = est.labels_  # 模型產生的分類標記

fig = plt.figure('f0', figsize=(5,4))  # 建立模型
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

# 用三個特徵值數列，畫出3D圖型上的點
ax.scatter(X[:, 3], X[:, 0], X[:,2],
           c=labels.astype(np.float), edgecolor='k')

# 畫出KMeans模型的重心
C = est.cluster_centers_
ax.scatter(C[:,3], C[:,0], C[:,2],
           c='red', s=30, alpha=0.5)

ax.w_xaxis.set_ticklabels([])   # 取消 x 軸刻度
ax.w_yaxis.set_ticklabels([])   # 取消 y 軸刻度
ax.w_zaxis.set_ticklabels([])   # 取消 z 軸刻度
ax.set_xlabel('Petal width')
ax.set_ylabel('Sepal length')
ax.set_zlabel('Petal length')
ax.set_title('k_means_iris_3')
ax.dist = 12    # 與3D圖的距離
plt.show()
