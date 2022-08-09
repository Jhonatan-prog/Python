import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('gas_prices.csv')

## First line
plt.plot(gas.Year, gas.Japan, label='Japan', color='red', linewidth=2)
## Second line
plt.plot(gas.Year,gas.Mexico, label='Mexico', color='green', linewidth=2, linestyle='--')

plt.title('Gas Graph/Gas-to-Time')
plt.xlabel('Years')
plt.ylabel('Gas')
plt.yticks([0.5,1,1.5,2,2.5,3,3.5,4,4.5,5])
plt.xticks(np.array(gas.Year[::3]))
plt.legend()
plt.show()