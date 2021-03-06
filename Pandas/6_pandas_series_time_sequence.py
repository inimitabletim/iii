import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(5),
               index=pd.date_range('20200101', periods=5))
print(ts)
print('')

ts = pd.Series(np.random.randn(5),
               index=pd.date_range('2020-01-01', periods=5, freq='M'))
print(ts)
print('')

ts = pd.Series(np.random.randn(5),
               index=pd.date_range('2020/01/01', periods=5, freq='W'))
print(ts)
print('')
