import numpy as np
from charts import draw_chart


def main() -> None:
    data = {
        'x': [13.0, 13.1, 13.2, 13.3, 13.4, 13.5, 13.6, 13.7, 13.8, 13.9],
        'y': [-0.00055, 0.447264, 0.871348, 1.226577, 1.473176, 1.581139, 1.533737, 1.329751, 0.984119, 0.526919],
    }

    x = np.array(data['x'])
    y = np.array(data['y'])

    draw_chart(x, y)


if __name__ == '__main__':
    main()
