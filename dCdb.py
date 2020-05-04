import numpy as np

'''
For a small network.
'''
# First define our sigma function.
sigma = np.tanh

# Next define the feed-forward equation.
def a1 (w1, b1, a0) :
  z = w1 * a0 + b1
  return sigma(z)

# The individual cost function is the square of the difference between
# the network output and the training data output.
def C (w1, b1, x, y) :
  return (a1(w1, b1, x) - y)**2

# This function returns the derivative of the cost function with
# respect to the weight.
def dCdw (w1, b1, x, y) :
  z = w1 * x + b1
  dCda = 2 * (a1(w1, b1, x) - y) # Derivative of cost with activation
  dadz = 1/np.cosh(z)**2 # derivative of activation with weighted sum z
  dzdw = x # derivative of weighted sum z with weight
  return dCda * dadz * dzdw # Return the chain rule product.

# This function returns the derivative of the cost function with
# respect to the bias.
# It is very similar to the previous function.
# You should complete this function.
def dCdb (w1, b1, x, y) :
  z = w1 * x + b1
  dCda = 2 * (a1(w1, b1, x) - y)
  dadz = 1/np.cosh(z)**2
  dzdb = 1
  return dCda * dadz * dzdb

# Testing the code.
# Let's start with an unfit weight and bias.
w1 = 2.3
b1 = -1.2
# We can test on a single data point pair of x and y.
x = 0
y = 1
# Output how the cost would change
# in proportion to a small change in the bias
print( dCdb(w1, b1, x, y) )

'''
For a larger network (ie has matrices and vectors).
'''
# Define the activation function.
sigma = np.tanh

# Let's use a random initial weight and bias.
W = np.array([[-0.94529712, -0.2667356 , -0.91219181],
              [ 2.05529992,  1.21797092,  0.22914497]])
b = np.array([ 0.61273249,  1.6422662 ])

# define our feed forward function
def a1 (a0) :
  # Notice the next line is almost the same as previously,
  # except we are using matrix multiplication rather than scalar multiplication
  # hence the '@' operator, and not the '*' operator.
  z = W @ a0 + b
  # Everything else is the same though,
  return sigma(z)

# Next, if a training example is,
x = np.array([0.1, 0.5, 0.6])
y = np.array([0.25, 0.75])

# Then the cost function is,
d = a1(x) - y # Vector difference between observed and expected activation
C = d @ d # Absolute value squared of the difference.
