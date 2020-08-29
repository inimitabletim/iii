
# --- 多維陣列的索引 page.47
import numpy as np

a = np.arange(16).reshape(2, 2, 4)

print(a)
print('')

# 切片擷取
print(a[0])
print('')

print(a[0, :, 1:3])
print('')

print(a[0, 1, :-1])
print('')

# 陣列索引
print(a[0, 1])
print('')

# 切片擷取
print(a[0][1])
print('')

# 陣列索引
print(a[0, 1, 2])
print('')

# 切片擷取
print(a[0][1][2])
print('')
