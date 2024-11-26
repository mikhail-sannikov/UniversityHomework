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

    # !!!
    n, a_exp, b_exp, sum_x, sum_y, sum_x2 = algorithms.first_approximation(x, y)
    sum_y_linear, sum_xy_linear = algorithms.second_approximation(x, y)

    a_linear, b_linear = algorithms.get_linear_values(n, sum_x, sum_y_linear, sum_xy_linear, sum_x2)
    y_approx_exp, y_approx_linear = algorithms.get_approximation_values(x, a_exp, a_linear, b_exp, b_linear)
    # !!!

    smoothed_exp, smoothed_linear = algorithms.get_smoothed_values(y_approx_exp, y_approx_linear)
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
        smoothed_exp,
        smoothed_linear,
        sigma_exp,
        sigma_linear,
    )


if __name__ == '__main__':
    main()
