import numpy as np


def f(x):
    return (x - 3)**2


def golden_section_search(trpl: np.ndarray, f) -> None:

    a = trpl[0]
    b = trpl[1]
    c = trpl[2]

    if not (f(b) < f(a) and f(b) < f(c)):
        return

    phi = (1 + np.sqrt(5)) / 2

    while c - a > 0.0001: # tolerance
        
        b = (c - a) / phi + a
        d = (a - c) / phi + c

        if f(b) > f(d):
            c = b
        else:
            a = d

        print(f"a: {a}, d: {d}, b: {b}, c: {c}")

    trpl[0] = a
    trpl[2] = c


def main():
    a = np.array([0, 2, 10])
    golden_section_search(a, f)

    print(a, f)


if __name__ == "__main__":
    main()
