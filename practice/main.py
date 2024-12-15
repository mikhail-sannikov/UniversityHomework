import math

# Константы
g = 9.81  # ускорение свободного падения, м/с^2
d = 200e-6  # диаметр частицы, м
rho = 1000  # плотность воды, кг/м^3
rho_s = 7874  # плотность железа, кг/м^3
mu = 0.014  # вязкость воды, Н·с/м^2


def f(v):
    Re = (rho * d * v) / mu  # число Рейнольдса
    Cd = 24 / Re + 3 / math.sqrt(Re) + 0.34  # коэффициент сопротивления
    lhs = g * (rho_s - rho) * d / (3 * Cd * rho)  # левая часть уравнения
    rhs = v**2  # правая часть уравнения
    return lhs - rhs


def find_interval(start, end, step=0.01):
    x = start

    while x < end:
        if f(x) * f(x + step) < 0:
            return x, x + step
        x += step

    raise ValueError('Нет интервала, в котором функция меняет знак')


def bisection_method(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) > 0:
        print("Функция имеет одинаковые знаки на концах интервала.")
        return None

    iter_count = 0

    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iter_count += 1

    return (a + b) / 2


def secant_method(v0, v1, tol=1e-6, max_iter=100):
    iter_count = 0

    while iter_count < max_iter:
        # Вычисляем следующее приближение по формуле метода секущих
        v2 = v1 - f(v1) * (v1 - v0) / (f(v1) - f(v0))

        if abs(v2 - v1) < tol:
            return v2

        v0, v1 = v1, v2
        iter_count += 1


def main():
    while True:
        match input('Хотите задать параметры самостоятельно? (y/n): ').lower():
            case 'y':
                print('Введите начальные приближение для метода половинного деления')
                a = float(input('Начальное приближение для нижней границы: '))
                b = float(input('Начальное приближение для верхней границы: '))
                bisection_max_iter = int(input('Максимальное число итераций: '))
                print('Введите начальные приближение для метода хорд')
                v0 = float(input('v0: '))
                v1 = float(input('v1: '))
                secant_max_iter = int(input('Максимальное число итераций: '))
            case 'n':
                a = 0.001
                b = 0.5
                bisection_max_iter = 100
                v0 = 0.01
                v1 = 0.1
                secant_max_iter = 100
            case _:
                continue
        break

    a, b = find_interval(a, b, 0.01)
    print(f'Интервал поиска корней: [{a}, {b}]')

    v_bisection = bisection_method(a, b, max_iter=bisection_max_iter)
    print(f"Метод половинного деления: v = {v_bisection:.8f} м/с")

    v_secant = secant_method(v0, v1, max_iter=secant_max_iter)
    print(f"Метод хорд: v = {v_secant:.8f} м/с")

    print(
        'Метод хорд быстрее'
        if v_secant < v_bisection
        else 'Метод половинного деления быстрее'
    )


if __name__ == '__main__':
    main()
