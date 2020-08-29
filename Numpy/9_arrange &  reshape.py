# --- 多維陣列的索引 page.46
import numpy as np
a = np.arange(0, 36).reshape(6, 6)
print(a)

print(a[4, 5])
print(a[4, -1])
print('')

print(a[3, 1:4])
print('')

print(a[:3, 3:])
print('')

print(a[2, :])
print('')

# 理論上應該是行向量,但 NumPy 輸出是列向量
print(a[:, 3])
print('')

print(a[:, ::2])
print('')

print(a[::2, ::3])