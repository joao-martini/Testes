import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3])
y = 2*x
z = 3*x


plt.figure()
plt.plot(x,y)
plt.plot(x,z)
plt.show()