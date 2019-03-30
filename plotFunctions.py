import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0., 4., 100)

plt.plot(x, x, label='x')
plt.plot(x, x**2, label='x squared') 
plt.plot(x, 2**x, label='2 to the power of x')
plt.ylabel('x')
plt.legend()
plt.show()