# --- 矩陣計算 page.50
import numpy as np

a = np.arange(6).reshape(3, 2)
print(a)
print('')

b = np.arange(6).reshape(2, 3)
print(b)
print('')

# 矩陣內積
c = np.dot(a, b)
print(c)
print('')

# 矩陣轉置
print(c.T)