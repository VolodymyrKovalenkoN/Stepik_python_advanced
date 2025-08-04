def pascal(number):
    p_list = []
    for i in range(number):
        if i == 0:
            p_list.append([1])
        else:
            sub_list = [1]
            for j in range(1, i):
                sub_list.append(p_list[i-1][j-1] + p_list[i-1][j])
            sub_list.append(1)
            p_list.append(sub_list)
    return p_list


n = int(input())
result = pascal(n)
for i in range(len(result)):
    print(*result[i])
