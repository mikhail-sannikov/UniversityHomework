import matplotlib.pyplot as plt
import numpy as np
from algorithms import newton_interpolation


def draw_chart(x: np.array, y: np.array) -> None:
    x_points = np.linspace(min(x), max(x), 500)
    y_points = [newton_interpolation(x, y, x_point) for x_point in x_points]

    plt.figure(figsize=(12, 8))
    plt.scatter(x, y, color='blue', zorder=5)
    plt.plot(x_points, y_points, label='Обратная интерполяция Ньютона', linestyle='--', color='blue')

    plt.title('Интерполяция Ньютона', fontsize=14)

    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)

    plt.legend(fontsize=12)
    plt.grid(True)

    plt.show()
