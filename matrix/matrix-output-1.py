# На вход программе подаются два натуральных числа 
# n и m, каждое на отдельной строке – количество строк и столбцов в матрице. 
# Далее вводятся сами элементы матрицы – слова, каждое на отдельной строке; 
# подряд идут элементы сначала первой строки, затем второй, и так далее.
# Напишите программу, которая сначала считывает элементы матрицы один за другим, 
# затем выводит их в виде матрицы.

row, column = int(input()), int(input())
matrix = []
for r in range(row):
    empty_row = []
    for j in range(column):
        empty_row.append(input())
    matrix.append(empty_row)

for r in range(row):
    for c in range(column):
        print(matrix[r][c], end=" ")
    print()
