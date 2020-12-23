# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

text_num = input('Введите целое положительное число ')

i = 1
max_num = int(text_num[0])

while i < len(text_num):
    if int(text_num[i]) > max_num:
        max_num = int(text_num[i])
    i += 1

print(f'Самая большая цифра: {max_num}')

print(f'А совсем просто так: {max(text_num)}')
