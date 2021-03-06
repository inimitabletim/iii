import pandas as pd

df = pd.read_csv('http://bit.ly/uforeports')

print(df.columns)
print('')

# ['City', 'Colors Reported', 'Shape Reported', 'State', 'Time']

print(df.count())
print('')

df1 = df[df.City.isnull()]

print(df1)
print('')

print(len(df1))
print('')

df = pd.read_csv('http://bit.ly/uforeports', usecols=[0,3,4])

print(df.head(5))
