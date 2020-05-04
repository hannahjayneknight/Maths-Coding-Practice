import numpy as np

'''
A very small neural network.
'''

# First we set the state of the network
s = np.tanh
w1 = 10
b1 = 0

# Then we define the neuron activation.
def a1(a0) :
  return s(w1 * a0 + b1)
  
# Finally let's try the network out!
# Replace x with 0 or 1 below,
a1(1)

'''
A larger neural network
'''
# First set up the network.
sigma = np.tanh
W = np.array([[-2, 4, -1],[6, 0, -3]])
b = np.array([0.1, -2.5])

# Define our input vector
x = np.array([0.3, 0.4, 0.1])

# Calculate the values by hand,
# and replace a1_0 and a1_1 here (to 2 decimal places)
# (Or if you feel adventurous, find the values with code!)
a1 = sigma( (W @ x) + b)
