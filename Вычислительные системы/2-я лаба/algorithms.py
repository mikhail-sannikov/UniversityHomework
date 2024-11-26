import numpy as np


def first_approximation(x, y):
    """Аппроксимация y = a * e^(b * x)"""

    x_exp = x[y > 0]
    y_exp = y[y > 0]

    # можно линеаризовать через логарифм
    n = len(x_exp)
    ln_y = np.log(y_exp)

    sum_x = np.sum(x_exp)
    sum_y = np.sum(ln_y)
    sum_x2 = np.sum(x_exp**2)
    sum_xy = np.sum(x_exp * ln_y)

    # метод наименьших квадратов
    b_exp = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
    ln_a = (sum_y - b_exp * sum_x) / n
    a_exp = np.exp(ln_a)

    return n, a_exp, b_exp, sum_x, sum_y, sum_x2


def second_approximation(x, y):
    """Аппроксимация y = a * x + b"""

    sum_y_linear = np.sum(y)
    sum_xy_linear = np.sum(x * y)

    return sum_y_linear, sum_xy_linear


def get_linear_values(n, sum_x, sum_y_linear, sum_xy_linear, sum_x2):
    a_linear = (n * sum_xy_linear - sum_x * sum_y_linear) / (n * sum_x2 - sum_x**2)
    b_linear = (sum_y_linear - a_linear * sum_x) / n

    return a_linear, b_linear


def get_approximation_values(x, a_exp, a_linear, b_exp, b_linear):
    """Вычисление аппроксимационных значений"""

    y_approx_exp = a_exp * np.exp(b_exp * x)
    y_approx_linear = a_linear * x + b_linear

    return y_approx_exp, y_approx_linear


def get_square_deviation(y, y_approx_exp, y_approx_linear):
    """Среднеквадратическое отклонение"""

    sigma_exp = np.sqrt(np.mean((y[y > 0] - y_approx_exp[y > 0]) ** 2))
    sigma_linear = np.sqrt(np.mean((y - y_approx_linear) ** 2))

    return sigma_exp, sigma_linear


def get_smoothed_values(y_approx_exp, y_approx_linear):
    smoothed_exp = get_moving_average(y_approx_exp, window_size=3)
    smoothed_linear = get_moving_average(y_approx_linear, window_size=3)

    return smoothed_exp, smoothed_linear


def get_moving_average(values, window_size=3):
    """Сглаживание (скользящее среднее) для аппроксимаций"""

    kernel = np.ones(window_size) / window_size
    average = np.convolve(values, kernel, mode='same')

    return average
