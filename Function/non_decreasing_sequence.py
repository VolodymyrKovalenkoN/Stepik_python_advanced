# Интересная сортировка-1
# На вход программе подается строка натуральных чисел. Из элементов строки формируется список чисел.
# Напишите программу сортировки списка чисел в порядке неубывания суммы их цифр.
# При этом, если два числа имеют одинаковую сумму цифр,
# следует сохранить их взаиморасположение в начальном списке.
# Формат входных данных
# На вход программе подается строка текста, содержащая натуральные числа, разделенные пробелами.
# Формат выходных данных
# Программа должна вывести отсортированный список чисел в соответствии с условием задачи,
# разделяя его элементы одним пробелом.

def number_converter(list_numbers):
    list_summa = []
    for number in list_numbers:
        if number // 10 == 0:
            list_summa.append(number)
        else:
            summa = 0
            while number // 10 != 0:
                summa += number % 10
                number = number // 10
            summa += number
            list_summa.append(summa)
    return list_summa


def sort_sequence(sum_list, original):
    l = len(sum_list)
    for i in range(l):
        swap = False
        for j in range(0, l - i - 1):
            if sum_list[j] > sum_list[j + 1]:
                sum_list[j], sum_list[j + 1] = sum_list[j + 1], sum_list[j]
                original[j], original[j + 1] = original[j + 1], original[j]
    return original


if __name__ == "__main__":
    numbers = [int(num) for num in input().split()]
    # print(number_converter(numbers))
    print(*sort_sequence(number_converter(numbers), numbers))
