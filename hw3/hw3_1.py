def division(a, b):
    c = a / b if b != 0 else 'На ноль делить нельзя!'
    return c

while True:
    num_str = (input('Введите два целых числа через пробел: ')).split()
    if num_str[0].isdigit() and num_str[1].isdigit():
        num1, num2 = int(num_str[0]), int(num_str[1])
        break

print(f'Результат деления: {division(num1, num2)}')

