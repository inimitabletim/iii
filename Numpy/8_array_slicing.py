
# --- 陣列切片 page.46
import numpy as np

# 一維陣列
a = np.arange(6)
print(a[2:-1])
print(a[::2])
print('')

# 二維陣列
a = np.array([[11, 12, 13], [23, 24, 25], [34, 35, 36]])
print(a)
print('')

print(a[1])
print(a[1:])
print(a[1][1:])
print('')

print(a[..., 1])   # ...代表省略
print(a[1, ...])
print(a[..., 1:])   # 第二列集剩下的所有元素
