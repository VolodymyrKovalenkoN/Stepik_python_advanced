def input_matrix(size):
    return [[int(el) for el in input().split()] for _ in range(size)]

n = int(input())
matrix = input_matrix(n)

max_element = max(matrix[i][j] for i in range(n) for j in range(i+1))
print(max_element) 