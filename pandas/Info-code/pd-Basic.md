[Documentation](https://pandas.pydata.org/docs/reference/frame.html)

.iloc: selects rows and columns at specific integer positions [rows,columns]
.loc : selects rows and columns with specific labels

### .iloc pandas sum

If you wanna sum two rows you need to select them and use **.sum(axis=1)** <br>
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
df.index.name = 'Index'
df['RamSum'] = df.iloc[:,1::6].sum(axis=1)
print(df)

```


### Changing boolean values with .loc
Firts parameter is the condition, the second is where you want the <br> 
do the change, then, specify the change.

```python
NaIndex = ['A','B','C','D']

## DataFrame
Info = {
    'Names': ['Alex','Camillo','Juan','Matias'], 
    'Age': [17,5,20,40],
    'Country': ['Venezuela','Colombia','USA','Peru'],
    'Merried': [False] * 4,
}

df = pd.DataFrame(Info, index=NaIndex)
df.loc[df['Age'] > 17, 'Merried'] = True
print(df.sample(1))
print()
print(df)

```

### Axes Iteration 

```python
df = pd.DataFrame(Info)
a=df.axes
for i in a[1]:
    print(i)

```

### A little of numpy

```python
NaIndex = ['A','B','C','D','E']

## DataFrame
Info = {
    'Names': ['Alex','Camillo','Juan','Matias'], 
    'Age': [17,5,20,40],
    'Country': ['Venezuela','Colombia','USA','Peru'],
    'Merried': [False] * 4,
}

df = pd.DataFrame(np.arange(15).reshape([5,3]), index=NaIndex, columns=['Z','X','Y'])
print(df)
```