from collections.abc import Callable

import numpy as np


def pattern_search(
    x: np.ndarray, s: float, f: Callable[[np.ndarray], np.ndarray], max_iter: int = 50
) -> np.ndarray:
    """Find the approximate minimum point of a function.

    Args:
        x: Coordinates of the starting point.
        s: Pattern size.
        f: Function.
        max_iter: Maximum amount of iterations.
    """

    for _ in range(max_iter):
        # pattern
        P = np.array([x, x + (-s, 0), x + (s, 0), x + (0, -s), x + (0, s)])

        fP = f(P.T)

        # index of the smallest element
        m = np.argmin(fP)

        if m == 0:
            s = s / 2
        else:
            x = P[m]

    return x


def main() -> None:
    f = lambda x: x[0] ** 2 + x[1] ** 2
    minimum = pattern_search(np.array([30, 43]), 8, f)
    print("Minimum: ", minimum)


if __name__ == "__main__":
    main()
