# Note: In the lecture exercise the variables 'x', 's' and the function 'f'
# are already predefined

P = np.array([x, x + (-s, 0), x + (s, 0), x + (0, -s), x + (0, s)])

fP = f(P)

m = np.argmin(fP)

if m == 0: 
    s = s / 2
else:
    x = P[m]
