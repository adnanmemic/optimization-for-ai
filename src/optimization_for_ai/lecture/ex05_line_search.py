# Note: In the homework assignment the variable 'x' (2-dim. np.array) the gradient 'df(x)' and the function 'f'
# are already predefined

d = -df(x)
alpha = 1.0

while f(x + alpha * d) >= f(x):
  alpha *= 0.7

x = x + alpha * d
