import math

import numpy as np

from icecream import ic

import algorithms


def main():
    A = np.array([
        [0, 4, 2, 2],
        [4, 8, 0, 2],
        [2, 0, 9, -4],
        [2, 2, -4, 12]
    ], dtype=float)
    A[0, 0] = 10 * 13 + 1

    B = np.array([
        2 * 13 * math.sin(13),
        5 * (math.sin(13) - math.cos(13)),
        7 * (math.cos(13) + math.sin(13)),
        3 * math.sin(13)
    ], dtype=float)

    A_copy = A.copy()
    B_copy = B.copy()

    x_gauss = algorithms.solve_by_gauss(A_copy, B_copy)

    omega_values = [1.0, 1.1, 1.25, 1.5]
    tol = 1e-6
    max_iterations = 1000

    # Проверка и коррекция матрицы
    if not algorithms.has_diagonal_dominance(A):
        print("Матрица не имеет диагонального преобладания. Производится коррекция")
        A_copy, B_copy = algorithms.make_diagonally_dominant(A.copy(), B.copy())

    x_sor = None

    for omega in omega_values:
        x_sor, iterations = algorithms.solve_by_sor(A_copy, B_copy, omega, tol, max_iterations)
        print(f"Решение найдено при ω={omega}: {x_sor}, число итераций: {iterations}")

        if x_sor is not None:
            break

    det_A = algorithms.get_determinant_lu(A)
    inv_A = algorithms.get_inverse_matrix(A)

    check_inv_A = algorithms.check_is_inv_matrix_right(A, inv_A)
    check_gauss = algorithms.check_solution(A, B, x_gauss)
    check_sor = algorithms.check_solution(A, B, x_sor)

    print('*' * 70)
    print("Решение методом Гаусса:", x_gauss)
    print("Решение методом SOR:", x_sor)
    print('*' * 70)
    print("Определитель матрицы A:", det_A)
    print("Обратная матрица A:")
    for row in inv_A:
        ic(row)
    print('*' * 70)
    print("Проверка корректности обратной матрицы:", check_inv_A)
    print("Проверка решения методом Гаусса:", check_gauss)
    print("Проверка решения методом SOR:", check_sor)


if __name__ == '__main__':
    main()
