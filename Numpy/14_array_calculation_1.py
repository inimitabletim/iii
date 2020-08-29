# --- 矩陣計算 page.49
import numpy as np

a = np.arange(6).reshape(2, 3)
print(a)
print('')

# 每個位置+5
print(a + 5)
print('')

b = np.ones(6, dtype=int).reshape(2, 3)

# 矩陣加法與純量乘法
print(a + 2 * b)