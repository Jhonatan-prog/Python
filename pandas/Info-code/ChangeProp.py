import numpy as np
import pandas as pd


index = np.array(["Japan","Colombia","Argentine","USA","Spain","Korea"])

infoPrices = {
    "Apple": [20,1,2,3,4,5],
    "Tangarine": [15,1,2,3,4,5],
    "Grapes": [20,1,2,3,4,5],
    "Watermelon": [50,1,2,np.nan,4,5],
    "Lemon": [5,1,2,3,4,5],
    "Banana": [10,2,3,4,5,2]
}

df = pd.DataFrame(infoPrices, index=pd.date_range("20220710", periods=len(infoPrices)))
print(df)