# Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

print('Программа обмена значений соседних элементов списка. Чтобы увидеть ее работу введите список, '
      'содержащий не меньше двух элементов.')

while True:
    str_list = input('Введите элементы списка через пробел: ')
    list_1 = str_list.split()
    if len(list_1) > 1:
        break
    print('\033[31m\033[7mВы ввели слишком мало элементов.\033[0m')

print(f'Исходный список: {list_1}')

for i, el, in enumerate(list_1):
    if (i - 1) % 2 == 0:
        list_1[i], list_1[i - 1] = list_1[i - 1], list_1[i]

print(f'Cписок после обмена: {list_1}')


