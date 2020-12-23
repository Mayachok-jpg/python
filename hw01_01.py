# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк
# и сохраните в переменные, выведите на экран.

text = input('Введите текст: ')
num_text = input('Введите число: ')

num = int(num_text)
boo = num < 0
num_float = 3*num / num

print('——*——'*20)

print (f'Это текст: {text}, тип {type(text)}')
print (f'Это тоже текст: {num_text}, тип {type(num_text)}')

print (f'А это уже число: {num}, тип {type(num)}')
print (f'Результат деления всегда float, даже если делится нацело: {num_float}, тип {type(num_float)}')
print (f'А это bool: {boo}, тип {type(boo)} ')
