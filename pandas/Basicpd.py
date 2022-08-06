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
