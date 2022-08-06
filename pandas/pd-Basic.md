### .iloc pandas sum

If you wanna sum two rows you need to select them and use **.sum(axis=1)**
axis 1 = ->
axis 0 = ↓ 

```python

from sqlite3 import Row
import numpy as np
import pandas as pd
import sys

NaIndex = ['A','B','C','D']

## DataFrame
a = {
    'Names': ['Alex','Camillo','Juan','Matias'], 
    'Age': [17,5,20,40],
    'x': [1,2,3,4],
    'Country': ['Venezuela','Colombia','USA','Peru'],
    'Merried': [False] * 4
}
df = pd.DataFrame(a, index=NaIndex)
# df['Sum'] = df['Age'] + df['x']
df['Sum'] = df.iloc[:,1:3].sum(axis=1)
print(df)

```