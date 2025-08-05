u_str = list(input().replace(" ",""))

pack_list = []

while u_str:
    cur_symbol = u_str[0]
    count = 1
    while count < len(u_str) and u_str[count] == cur_symbol:
        count += 1
    pack_list.append(u_str[:count])
    u_str = u_str[count:]

print(pack_list)

