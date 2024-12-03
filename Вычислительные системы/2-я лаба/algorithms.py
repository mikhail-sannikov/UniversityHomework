import numpy as np


def first_approximation(n, x, sum_x, sum_x2, sum_y, sum_xy):
    """Аппроксимация y = a * e^(b * x)"""

    b_exp = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    ln_a = (sum_y - b_exp * sum_x) / n
    a_exp = np.exp(ln_a)

    return a_exp * np.exp(b_exp * x), a_exp, b_exp


def second_approximation(n, x, y, sum_x, sum_x2):
    """Аппроксимация y = a * x + b"""

    sum_y_linear = np.sum(y)
    sum_xy_linear = np.sum(x * y)

    a_linear = (n * sum_xy_linear - sum_x * sum_y_linear) / (n * sum_x2 - sum_x ** 2)
    b_linear = (sum_y_linear - a_linear * sum_x) / n

    return a_linear * x + b_linear, a_linear, b_linear


def get_square_deviation(y, y_approx_exp, y_approx_linear):
    """Среднеквадратическое отклонение"""

    sigma_exp = np.sqrt(np.mean((y[y > 0] - y_approx_exp[y > 0]) ** 2))
    sigma_linear = np.sqrt(np.mean((y - y_approx_linear) ** 2))

    return sigma_exp, sigma_linear
