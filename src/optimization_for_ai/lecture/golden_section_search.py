# Note: In the lecture exercise the variable 'trpl' and the function 'f'
# are already predefined

(a, b, c) = trpl

phi = (1 + np.sqrt(5)) / 2

if b - a > c - b:

    d = (a - c) / phi + c

    if f(d) < f(b):
        # new triple: (a, d, b)
        c = b
        b = d
    else:
        # new triple: (d, b, c)
        a = d
else:
    d = (c - a) / phi + a

    if f(d) < f(b):
        # new triple: (b, d, c)
        a = b
        b = d
    else:
        # new triple: (a, b, d)
        c = d

trpl[:] = a, b, c
