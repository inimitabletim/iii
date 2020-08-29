# --- 廣播(Broadcast) page.49
import numpy as np

a = np.array([[1, 2, 3, 4], [4, 5, 6, 7]])
b = np.random.randint(1, 3, 8).reshape(2, 4)

print(a)
print('')

# 形狀一樣
print(b)
print('')

print(a*b)
print('')

# 乘法廣播
c = np.array([1, 2]).reshape(2, 1)
print(c)
print('')

print(a*c)
print('')

# 加法廣播
d = np.array([1, 1, 1, 1])
print(a+d)