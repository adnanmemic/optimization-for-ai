# Note: In the lecture exercise the variables 'X' (3x2-dim. np.array) and the function 'f'
# are already predefined

fX = f(X.T)

qr = 0.99
qe = 1.95
qc = 0.33

a = (X[0] + X[1]) / 2 # zentroid
r = a + qr * (a - X[2]) # reflection
e = a + qe * (a - X[2]) # expansion
c = a - qc * (a - X[2]) # contraction

if f(r) < fX[2] and f(r) < f(e) and f(r) < f(c):
  # reflection
  X = np.array([X[0], X[1], r])
elif f(e) < fX[2] and f(e) < f(c):
  # expansion
  X = np.array([X[0], X[1], e])
elif f(c) < fX[2]:
  # contraction
  X = np.array([X[0], X[1], c])
else:
  # shrink
  X = (X + X[0]) / 2
  
# sort array to ensure that the wort point is the last element
fX = f(X.T)
X = X[np.argsort(fX)]
