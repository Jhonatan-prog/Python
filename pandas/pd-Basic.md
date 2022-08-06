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


### Unsing .iloc flawless
```python
import numpy as np
import pandas as pd
import sys

NaIndex = ['A','B','C','D']

## DataFrame
Info = {
    'Names': ['Alex','Camillo','Juan','Matias'], 
    'Age': [17,5,20,40],
    'Country': ['Venezuela','Colombia','USA','Peru'],
    'x': [1,2,3,4],
    'Merried': [False] * 4,
    'n': [1,2,3,4],
    'z': [1,2,3,4]
}

df = pd.DataFrame(Info, index=NaIndex)
df['RamSum'] = df.iloc[:,1::6].sum(axis=1)
print(df)

```