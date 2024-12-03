import algorithms
import numpy as np
from charts import draw_chart


def main() -> None:
    data = {  # noqa
        'x': [13.0, 13.1, 13.2, 13.3, 13.4, 13.5, 13.6, 13.7, 13.8, 13.9],
        'y': [-0.00055, 0.447264, 0.871348, 1.226577, 1.473176, 1.581139, 1.533737, 1.329751, 0.984119, 0.526919],
    }

    x = np.array(data['x'])
    y = np.array(data['y'])

    x_exp = x[y > 0]  # поскольку логарифм можно взять только от положительных значений
    y_exp = y[y > 0]

    n = len(x_exp)
    ln_y = np.log(y_exp)  # линеаризуем через логарифм для МНК

    sum_x = np.sum(x_exp)
    sum_y = np.sum(ln_y)
    sum_x2 = np.sum(x_exp ** 2)
    sum_xy = np.sum(x_exp * ln_y)

    # аппроксимация методом наименьших квадратов
    y_approx_exp, a_exp, b_exp = algorithms.first_approximation(n, x, sum_x, sum_x2, sum_y, sum_xy)
    y_approx_linear, a_linear, b_linear = algorithms.second_approximation(n, x, y, sum_x, sum_x2)

    sigma_exp, sigma_linear = algorithms.get_square_deviation(y, y_approx_exp, y_approx_linear)

    print('y = a * e^(b * x):')
    print(f'a = {a_exp:.6f} | b = {b_exp:.6f}')
    print(f'Среднеквадратичное отклонение: {sigma_exp:.6f}\n')

    print('y = a * x + b:')
    print(f'a = {a_linear:.6f} | b = {b_linear:.6f}')
    print(f'Среднеквадратичное отклонение: {sigma_linear:.6f}\n')

    draw_chart(
        x,
        y,
        y_approx_exp,
        y_approx_linear,
        a_exp,
        a_linear,
        b_exp,
        b_linear,
        sigma_exp,
        sigma_linear,
    )


if __name__ == '__main__':
    main()
