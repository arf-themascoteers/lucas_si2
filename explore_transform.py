import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/dataset_min.csv")

signal = df.iloc[0].to_numpy()

start_index = list(df.columns).index("400")

signal = signal[start_index:]
x = np.arange(len(signal))

plt.figure()
plt.plot(x, signal, 'o', label='Bands', markersize=2)
plt.xlabel('i')
plt.ylabel('b(i) ')
#plt.title('Cubic Spline Interpolation')
plt.legend()
plt.grid(True)
plt.show()

ref = 1/(10**signal)

plt.figure()
plt.plot(x, ref, 'o', label='Bands', markersize=2)
plt.xlabel('i')
plt.ylabel('b(i) ')
#plt.title('Cubic Spline Interpolation')
plt.legend()
plt.grid(True)
plt.show()