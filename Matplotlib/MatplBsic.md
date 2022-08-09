[Matplotlib_Documentation](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.html)

## Basic about matplotlib

### Commands
The **axes** need the same shape
plt.plot(axis x, axis y, *label*,*color*,*linewidth*,*marker='.'*,*markersize*,*linestyle*)

This will change the graph size
plt.xticks([array])
plt.yticks([array])

**fontdict** is use to change the font properties

[Short hand](https://matplotlib.org/2.1.2/api/_as_gen/matplotlib.pyplot.plot.html) to use in plt.plot()

## Using panda, numpy and matplotlib in real life

```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

gas = pd.read_csv('gas_prices.csv')

## First line
plt.plot(gas.Year, gas.Japan, label='Japan', color='red', linewidth=2)
## Second line
plt.plot(gas['Year'],gas['Mexico'], label='Mexico', color='green', linewidth=2, linestyle='--')

plt.title('Gas Graph/Gas-to-Time')
plt.xlabel('Years')
plt.ylabel('Gas')
plt.yticks([0.5,1,1.5,2,2.5,3,3.5,4,4.5,5])

## gas.Year[we don't care where it stars, from 0 to max len, skipping 3 by 3]
## plt.xticks(gas.Year[::3])
plt.xticks(np.array(gas.Year[::3]))
plt.legend()

plt.savefig('Gas Graph', dpi=300)

plt.show()

```