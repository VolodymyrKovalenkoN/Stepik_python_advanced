n = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(n)

for i in range(len(n)):
    for j in range(len(n)):
        print(n[j][i], end=" ")
    print()