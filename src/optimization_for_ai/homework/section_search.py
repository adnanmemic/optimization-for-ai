# Note: In the homework assignment the variable 'trpl' and the function 'f'
# are already predefined

(a, b, c) = trpl

if b - a > c - b:
    d = a + (b - a) * ((f(a) - f(c)) / ((max(f(c), f(a)) - f(b)) * 2.1) + 0.5)

    if f(d) < f(b):
        # new triple: (a, d, b)
        c = b
        b = d
    else:
        # new triple: (d, b, c)
        a = d
else:
    d = c + (b - c) * ((f(c) - f(a)) / ((max(f(c), f(a)) - f(b)) * 2.1) + 0.5)

    if f(d) < f(b):
        # new triple: (b, d, c)
        a = b
        b = d
    else:
        # new triple: (a, b, d)
        c = d

trpl[:] = a, b, c
