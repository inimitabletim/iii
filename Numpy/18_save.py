# --- 存檔 page.51
import numpy as np

a = np.random.randint(1, 20, 16).reshape(4, 4)
print(a)
print('')

b = np.sort(a, axis=0)
print(b)
print('')

c = np.sort(b, axis=0)
print(c)
print('')

np.save('c', c)
np.savetxt('c', c)

d = np.load('c.npy')
print(d)