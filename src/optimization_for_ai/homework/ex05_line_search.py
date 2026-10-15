# Note: In the homework assignment the variable 'x' (2-dim. np.array) the 
# gradient 'df(x)' and the function 'f' are already predefined

alpha = 0.96

x_arrow = x - alpha * df(x) - alpha * df(x - alpha * df(x))

# matrixmultiplication because with the transposition the column vector becomes a row vector
while f(x_arrow) >= f(x) or f(x_arrow) - f(x) > 0.29 * (x_arrow - x).T @ df(x):
  alpha *= 0.45
  x_arrow = x - alpha * df(x) - alpha * df(x - alpha * df(x))

x = x_arrow
