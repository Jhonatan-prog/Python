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

Serie1 = pd.Series(['Apple','Pineaple','Banana','Watermelon'])
df = pd.DataFrame(Info, index=NaIndex)
df.to_csv('NewInfo')
print(df)