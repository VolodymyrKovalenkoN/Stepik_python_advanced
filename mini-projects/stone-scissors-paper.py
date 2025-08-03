# Камень, ножницы, бумага

timur, ruslan = input(), input()
sete = ["камень", "ножницы", "бумага"]
result = ["Тимур", "Руслан", "ничья"]
if timur == ruslan:
    result = result[2]
elif timur == sete[0]:
    if ruslan == sete[1]:
        result = result[0] # По камню выиграл у ножниц Тимур
    else:
        result = result[1]
elif timur == sete[1]:
    if ruslan == sete[2]:
        result = result[0] # По ножницам выиграл у бумаги Тимур
    else:
        result = result[1]
elif timur == sete[2]:
    if ruslan == sete[0]:
        result = result[0] # По бумаге выиграл у камня Тимур
    else:
        result = result[1]
print(result)