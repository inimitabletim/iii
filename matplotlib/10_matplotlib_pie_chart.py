import matplotlib.pyplot as plt
import numpy as np

labels = ['Q1', 'Q2', 'Q3', 'Q4']
sizes = [20, 30, 40, 10]
explode = (0, 0.1, 0, 0)

plt.axis('equal') # 圓形

cmap = plt.cm.magma
colors = cmap(np.linspace(0., 1., len(labels)* 1))
wedges, texts, autotexts = plt.pie(sizes, colors=colors, explode=explode,
                                  labels=labels, autopct='%1.2f%%',
                                   shadow = False, startangle = 90)
plt.setp(autotexts, size=8, weight='bold', color='white')
plt.setp(texts, size=8, weight='bold')
plt.title('Pie Chart', weight='bold')

plt.show()