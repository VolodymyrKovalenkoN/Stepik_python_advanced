# Больше среднего
# Напишите программу, которая выводит количество элементов квадратной матрицы в 
# каждой строке, больших среднего арифметического элементов данной строки.
# Формат входных данных
# На вход программе подается натуральное число 
# n – количество строк и столбцов в матрице, затем элементы матрицы 
# (целые числа) построчно через пробел.

def input_matrix(size):
    matrix = []
    for i in range(size):
        sub = [int(i) for i in input().split()]
        matrix.append(sub)
    return matrix

def above_average(u_matrix):
    return [sum(1 for el in row if el > sum(row)/len(row)) for row in matrix]

m_size = int(input())

matrix = input_matrix(m_size)
print(above_average(matrix))