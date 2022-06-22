import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

x = np.array([1,2,3])
y = 2*x
z = 3*x
w = 7*x
t = 1*x
v = 9*x

plt.figure()
plt.plot(x,y)
plt.plot(x,z)
plt.show()