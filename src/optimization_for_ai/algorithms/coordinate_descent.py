from collections.abc import Callable

import sympy as sp


def coordinate_descent(
    x: float, y: float, f: Callable[[sp.Expr, sp.Expr], sp.Expr], max_iter: int = 50
) -> tuple[float, float]:
    """Find the approximate minimum point of a function.

    Args:
        x: Starting x-coordinate.
        y: Starting y-coordinate.
        f: Function supporting symbolic inputs.
        max_iter: Maximum number of coordinate updates.
    """
    sx, sy = sp.symbols("x,y")
    expression = f(sx, sy)

    for i in range(max_iter):
        if i % 2 == 0:
            diff = sp.diff(expression, sx)
            equation = sp.Eq(diff.subs(sy, y), 0)
            x = sp.solve(equation, sx)[0]
        else:
            diff = sp.diff(expression, sy)
            equation = sp.Eq(diff.subs(sx, x), 0)
            y = sp.solve(equation, sy)[0]

    return float(x), float(y)


def main() -> None:
    f = lambda x, y: 4 * x**2 + 3 * y**2 + 2 * x - x * y
    print(f"Minimum: {coordinate_descent(50, 4, f)}")


if __name__ == "__main__":
    main()
