# След матрицы ↘️
# Следом квадратной матрицы называется сумма элементов главной диагонали. 
# Напишите программу, которая выводит след заданной квадратной матрицы.
# Формат входных данных
# На вход программе подается натуральное число 
# n – количество строк и столбцов в матрице, затем элементы матрицы 
# (целые числа) построчно через пробел.

def main_diagonal(size):
    matrix = []
    for i in range(size):
        sub = [int(i) for i in input().split()]
    matrix.append(sub)
    return matrix

def matrix_trace(matrix):
    # sum = 0
    # for i in range(n):
    #     for j in range(n):
    #         sum += matrix[i][j]
    return sum(matrix[i][i] for i in range(n))


n = int(input())

u_matrix = main_diagonal(n)
print(matrix_trace(u_matrix))


