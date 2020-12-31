# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(num1, num2, num3):
    num_list = sorted([num1, num2, num3])
    print(num_list)
    return (num_list[1] + num_list[2])

print(my_func(4, 6, 2))