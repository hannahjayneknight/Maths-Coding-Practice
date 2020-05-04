# need to change the function for what you need

def f (x) :
  return x**6/6 - 3*x**4 - 2*x**3/3 + 27*x**2/2 + 18*x - 30

def d_f (x) :
  return x**5 - 12*x**3 - 2*x** 2 + 27*x + 18

x = -4.0

d = {"x" : [x], "f(x)": [f(x)]}
for i in range(0, 20):
  x = x - f(x) / d_f(x)
  d["x"].append(x)
  d["f(x)"].append(f(x))

pd.DataFrame(d, columns=['x', 'f(x)'])

'''
Some starting points on the curve do not converge, nor do they diverge, but oscillate without settling.

Again, this is behaviour that happens in areas where the curve is not well described by a straight line - therefore our 
initial linearisation assumption was not a good one for such a starting point.

In practice, often you will not need to hand craft optimisation methods, as they can be called from libraries, such as scipy.
'''