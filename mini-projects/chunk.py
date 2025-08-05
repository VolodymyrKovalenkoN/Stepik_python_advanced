u_str, n = input().split(), int(input())
u_len = len(u_str)
c_list = []

chucnk = u_len // n

while chucnk:
    c_list.append(u_str[:n])
    u_str = u_str[n:]
    chucnk -= 1
if u_str:
    c_list.append(u_str)
print(c_list)