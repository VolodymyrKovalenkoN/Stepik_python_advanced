# # Напишите функцию func_apply(), принимающую на вход функцию и список значений и возвращающую список,
# # в котором каждое значение будет результатом применения переданной функции к переданному списку.
# Skriv ein funksjon func_apply() som tek inn ein funksjon og ei liste med verdiar,
# og returnerer ei liste der kvar verdi er resultatet av å bruke den gitte funksjonen på den gitte lista.

def func_apply(func, iter_obj):
    return [func(item) for item in iter_obj]

def multi(number):
    return number*5

print(func_apply(multi, [1, 2, 3, 4, 5]))
