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

a = np.array([4,5,6])
b = 2*a
c = np.array([4,5,6])
d = 3*c

plt.figure()
plt.plot(x,y)
plt.plot(x,z)
plt.show()