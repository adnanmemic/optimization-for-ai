# Note: In the lecture exercise the variables 'X' (3x2-dim. np.array) and the function 'f'
# are already predefined

fX = f(X.T)

# X[0] and X[1] are the two better points whereas X[2] is the worst
# that is also the reason why sorting is important 

a = (X[0] + X[1]) / 2 # zentroid
r = a + (a - X[2]) # reflection

if f(r) < fX[2]:
  # reflection
  X = np.array([X[0], X[1], r])
else:
  # shrink
  X = (X + X[0]) / 2

# sort array to ensure that the wort point is the last element
fX = f(X.T)
X = X[np.argsort(fX)]
