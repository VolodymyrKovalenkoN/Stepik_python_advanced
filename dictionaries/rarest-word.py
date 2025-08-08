# Самое редкое слово 🌶️
# На вход программе подается строка текста. 
# Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра. 
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

u_string = input().lower().split()
signs = ".,!?:;- "
clear_str = []
for word in u_string:
    if len(word)>1 and word[-1] in signs:
        word = word[:-1]
        clear_str.append(word)
    elif len(word) == 1 and word in signs:
        continue
    else:
        clear_str.append(word)
result = {}

# Подсчет частоты слов
for word in clear_str:
    if word not in result:
        result[word] = clear_str.count(word)

# Находим минимальную частоту
min_freq = min(result.values())

# Находим лексикографически минимальное слово среди слов с минимальной частотой
min_word = min([word for word, freq in result.items() if freq == min_freq])

print(min_word)