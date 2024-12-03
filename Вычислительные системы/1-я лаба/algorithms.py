from math import factorial

import numpy as np


def newton_interpolation(x: np.array, y: np.array, x_point: float) -> None:
    """Интерполяция Ньютона с факториалами"""

    n = len(x)
    h = x[1] - x[0]
    q = (x_point - x[-1]) / h

    # Вычисление конечных разностей
    diff_table = np.zeros((n, n))
    diff_table[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            diff_table[i, j] = diff_table[i + 1, j - 1] - diff_table[i, j - 1]

    # Интерполяция
    result = y[-1]
    t = 1

    for i in range(1, n):
        t *= q + i - 1
        result += (t / factorial(i)) * diff_table[n - i - 1, i]

    return result
