# --- 等差數列與等比數列 page.45
import numpy as np

a = np.linspace(10, 20, 5, endpoint=False)
print(a)

b = np.linspace(0, 2, 9).reshape(3, 3)
print(b)

c = np.logspace(0, 9, 10, base=2, dtype='i4').reshape(2, 5)
print(c)