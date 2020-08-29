import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#鳥王隨機產生100個棲息座標x_data
x_data = np.random.rand(100).astype(np.float32)

# 鳥王的指令
y_data = x_data * 8
#然而飛鳥棲息位置，會與實際有所偏移，偏移值noise_data
noise_data = np.random.normal(0.0, 0.5, 100).astype(np.float32)

# 統計100點實際飛鳥棲息的偏移值
plt.hist(noise_data)
plt.show()
