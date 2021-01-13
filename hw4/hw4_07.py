def fact(n):
    factorial = 1
    for el in range(1, n + 1):
        factorial *= el
        yield factorial
n = None
while n == None:
    text = input('Факториал какого числа посчитать? ')
    n = int(text) if text.isdigit() else None

for el in fact(n):
    print(el)

