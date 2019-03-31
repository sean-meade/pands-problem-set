# Question 10
"""
TO DO:
"""
# import matplotlib to plot graphs
import matplotlib.pyplot as plt
# and numpy to hold data
import numpy as np

# Set variable x to the array of 0 to 4 with 100ms seperation.
x = np.linspace(0., 4., 100)
# Plot x with label x
plt.plot(x, x, label='x')
# Plot x^2 with label x^2
plt.plot(x, x**2, label='x squared')
# Plot 2^x with label 2^x
plt.plot(x, 2**x, label='2 to the power of x')
# Label y-axis
plt.ylabel('x')
# Plot legend of labels
plt.legend()
# Plot the graph
plt.show()