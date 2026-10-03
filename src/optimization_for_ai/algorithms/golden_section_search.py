from collections.abc import Callable

import numpy as np


def golden_section_search(
    precision, trpl: np.ndarray, f: Callable[[float], float]
) -> None:

    (a, b, c) = trpl

    # golden ratio
    phi = (1 + np.sqrt(5)) / 2

    if not (f(b) < f(a) and f(b) < f(c)):
        return

    while c - a > precision:
        # check whether d is placed to the left or right of b
        if b - a > c - b:
            d = (a - c) / phi + c

            # compare the function values of b and d
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


def main():
    trpl = np.array([0, 4, 10], dtype=float)
    golden_section_search(0.0001, trpl, lambda x: (x - 3) ** 2)
    print(f"New triple: {trpl}")
    print(f"Minimum is: {int(trpl[1])}")


if __name__ == "__main__":
    main()
