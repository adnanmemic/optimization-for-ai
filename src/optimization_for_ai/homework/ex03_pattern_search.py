# Note: In the homework assignment the variable x, d and the function 'f'
# are already predefined

P = np.array([x, x - d, x + d + (d[1], -d[0]), x + d + (-d[1], d[0])])

fP = np.array([f(i) for i in P])

m = np.argmin(fP)

if m == 0:
    d = d / 2
else:
    x_prev = x
    x = P[m]
    d = x - x_prev
