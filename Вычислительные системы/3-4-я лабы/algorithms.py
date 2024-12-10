import numpy as np


def solve_by_gauss(A, B):
    n = len(B)

    # Прямой ход
    for i in range(n):
        # Поиск максимального элемента для улучшения устойчивости
        max_row = max(range(i, n), key=lambda r: abs(A[r, i]))
        A[[i, max_row]] = A[[max_row, i]]
        B[i], B[max_row] = B[max_row], B[i]

        # Приведение к треугольному виду
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]
            B[j] -= factor * B[i]

    # Обратный ход
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (B[i] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x


def solve_by_sor(A, b, omega, tol, max_iterations):
    n = len(b)
    x = np.zeros_like(b)

    for iteration in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            sum1 = np.dot(A[i, :i], x_new[:i])
            sum2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (1 - omega) * x[i] + (omega / A[i, i]) * (b[i] - sum1 - sum2)
        error = np.linalg.norm(x_new - x, ord=np.inf)
        if error < tol:
            return x_new, iteration + 1
        x = x_new

    return None, None


def has_diagonal_dominance(A):
    for i in range(len(A)):
        if abs(A[i, i]) < sum(abs(A[i, j]) for j in range(len(A)) if j != i):
            return False
    return True


def make_diagonally_dominant(A, B):
    n = len(A)
    for i in range(n):
        row_sum = sum(abs(A[i, j]) for j in range(n) if j != i)
        if abs(A[i, i]) < row_sum:
            A[i, i] = row_sum + 1
    return A, B


def lu_decomposition(matrix):
    size = len(matrix)
    L = np.zeros((size, size))
    U = np.zeros((size, size))

    for i in range(size):
        # Верхняя треугольная матрица U
        for j in range(i, size):
            U[i, j] = matrix[i, j] - np.dot(L[i, :i], U[:i, j])

        # Нижняя треугольная матрица L
        for j in range(i, size):
            if i == j:
                L[i, j] = 1  # Диагональные элементы L равны 1
            elif U[i, i] != 0:  # Проверка деления
                L[j, i] = (matrix[j, i] - np.dot(L[j, :i], U[:i, i])) / U[i, i]

    return L, U


def get_determinant_lu(matrix):
    _, U = lu_decomposition(matrix)
    det = 1

    for i in range(len(U)):
        det *= U[i][i]

    return det


def get_inverse_matrix(A):
    n = len(A)
    A_copy = A.copy()
    identity = np.eye(n)

    for i in range(n):
        # Поиск максимального элемента
        max_row = max(range(i, n), key=lambda r: abs(A_copy[r, i]))
        if i != max_row:
            A_copy[[i, max_row]] = A_copy[[max_row, i]]
            identity[[i, max_row]] = identity[[max_row, i]]

        # Нормализация строки
        diag_element = A_copy[i, i]
        A_copy[i] /= diag_element
        identity[i] /= diag_element

        for j in range(n):
            if i != j:
                factor = A_copy[j, i]
                A_copy[j] -= factor * A_copy[i]
                identity[j] -= factor * identity[i]

    return identity


def check_solution(A, B, x):
    n = len(B)
    result = [sum(A[i][j] * x[j] for j in range(n)) for i in range(n)]
    return all(abs(result[i] - B[i]) < 1e-9 for i in range(n))


def check_is_inv_matrix_right(A, inv_A):
    return np.allclose(np.dot(A, inv_A), np.eye(len(A)))
