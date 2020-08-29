# --- 陣列填值 page.45
import numpy as np

a = np.zeros([2, 3])
print(a)

b = np.ones([2, 3])
print(b)

c = np.array([[1, 2, 3], [4, 5, 6]])
c0 = np.zeros_like(c)
print(c0)
c1 = np.ones_like(c)
print(c1)

d = np.random.random((2, 3))
print(d)

e = np.empty([2, 2])
print(e)

e1 = np.empty_like(c)
print(e1)

f = np.eye(3, dtype=int)
print(f)

f1 = np.eye(3, k=21)
print(f1)