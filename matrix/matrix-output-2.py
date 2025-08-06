# На вход программе подаются два натуральных числа 
# n и m, каждое на отдельной строке — количество строк и столбцов в матрице. 
# Далее вводятся сами элементы матрицы – слова, каждое на отдельной строке; подряд идут 
# элементы сначала первой строки, затем второй, и так далее.
# Напишите программу, которая считывает элементы матрицы один за другим, 
# выводит их в виде матрицы, выводит пустую строку, и снова ту же матрицу, 
# но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так далее.
# Формат входных данных

def enter_matrix(row, column):
    matrix = []
    for i in range(row):
        empty_row = []
        for j in range(column):
            empty_row.append(input())
        matrix.append(empty_row)
    return matrix

def row_to_col(matrix):
    r_matrix = []
    for i in range(len(matrix[0])):
        sub = []
        for j in range(len(matrix)):
            sub.append(matrix[j][i])
        r_matrix.append(sub)
    return r_matrix

def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end=" ")
        print()

rows, columns = int(input()), int(input())

m = enter_matrix(rows, columns)
print_matrix(m)
print()
reverse = row_to_col(m)
print_matrix(reverse)
