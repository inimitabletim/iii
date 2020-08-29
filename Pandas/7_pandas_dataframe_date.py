import pandas as pd
import numpy as np

d = { 'A' : pd.Series(data=np.random.randint(10,30,5), index=pd.date_range('20200101',periods=5)),
      'B' : pd.Series(data=np.random.randint(50,80,5), index=pd.date_range('20200101',periods=5)),
      'C' : pd.Series(data=np.random.randint(100,150,5), index=pd.date_range('20200101',periods=5)) }

df = pd.DataFrame(d, index=pd.date_range('20200101',periods=5))
print(df)
print('')

df['D'] = df['B'] + df['C']  #欄與欄進行運算
print(df)
print('')

print(df.loc['20200102':'20200104'])  #按日期區間擷取
print('')

del df['A']  #刪除 A欄
print(df)
print('')

df['E'] = pd.Series(data=[10,20,30,40,50],     #增加 E欄
                    index=pd.date_range('20200101',periods=5))
print(df)
print('')

print(df['B'].values)  # B欄的值
print('')

print(df.T) #轉置
print('')


df = df.drop(pd.to_datetime('20200101')) #刪除 row index = 20200101
print(df)
print('')

df = df.drop(pd.date_range('20200103',periods=2))  #刪除2列
print(df)
print('')

d = { 'B': 10, 'C': 20, 'D': 30, 'E': 40, }  #增加 1 列
df = df.append(pd.DataFrame(data=d ,index=pd.date_range('20200106',periods=1)), sort=True)

d = [{ 'B': 11, 'C': 21, 'D': 31, 'E': 41, },
     { 'B': 32, 'C': 22, 'D': 32, 'E': 42, }]    #增加 2 列
df = df.append(pd.DataFrame(data=d ,index=pd.date_range('20200107',periods=2)), sort=True)


print(df)
print('')

