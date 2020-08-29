# --- Matplotlib pyplot page.60
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 200)
y = np.sin(x)

# 原始的圖案
plt.plot(x, y)
plt.show()

# 線條 顏色 寬度 樣式
plt.plot(x, y, color='blue', linewidth=1.0, linestyle='--')

# 增加坐標軸長度
plt.xlim(x.min()*1.2, x.max()*1.2)
plt.ylim(y.min()*1.2, y.max()*1.2)

# 座標刻度(Latex)
plt.xticks((-np.pi, -np.pi/2, np.pi/2, np.pi), (r'$-\pi$', r'$-\pi/2$', r'$+\pi/2$', r'$+\pi$'))
plt.yticks([-1, -0.5, 0, 0.5, 1])

# 取得目前座標軸
g = plt.gca()

g.spines['right'].set_color('none')   # 隱藏右框線
g.spines['top'].set_color('none')   # 隱藏上框線
