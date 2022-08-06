import numpy as np
import pandas as pd
import sys

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
print(df)