# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

import colorama
colorama.init()

diff_list = [1, 2.3, True, 5 + 6j, 'Hello, Python!',  b'Text', None,
            [1, 'a', 'b', 'c'], (1, 2, True), {1, 2, 3, '4'},
            {'name': 'Tom', 'age' : 5}
            ]

print(f'{(colorama.Fore.GREEN + "Элемент списка").ljust(34)}  {colorama.Fore.BLACK + "|"} {colorama.Fore.GREEN + "Его тип"}')
print(colorama.Style.RESET_ALL, end='')
print('—'*50)
for el in diff_list:
    print(f'{str(el).ljust(30)} {"|"} {type(el)}')


