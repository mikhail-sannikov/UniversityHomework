import matplotlib.pyplot as plt


def draw_chart(
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
) -> None:
    plt.figure(figsize=(12, 6))
    plt.scatter(x, y, label='Исходные данные', color='blue')

    plt.plot(
        x,
        y_approx_exp,
        label=f'Экспоненциальная аппроксимация: y = {a_exp:.3f} * e^({b_exp:.3f}x), σ = {sigma_exp:.3f}',
        color='green',
    )
    plt.plot(x, smoothed_exp, label='Сглаженная экспоненциальная аппроксимация', color='lightgreen', linestyle='dashed')

    plt.plot(
        x,
        y_approx_linear,
        label=f'Линейная аппроксимация: y = {a_linear:.3f}x + {b_linear:.3f}, σ = {sigma_linear:.3f}',
        color='red',
    )
    plt.plot(x, smoothed_linear, label='Сглаженная линейная аппроксимация', color='orange', linestyle='dashed')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Аппроксимация данных и сглаживание')
    plt.legend()
    plt.grid()
    plt.show()
