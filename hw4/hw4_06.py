from itertools import count, cycle

n = None
fin = None

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

while n == None:
    text = input('С какого числа начать? ')
    n = int(text) if is_digit(text) else None

print(n)

while fin == None:
    text = input('На каком закончить? ')
    fin = int(text) if is_digit(text) else None
    if fin != None and fin < n:
        print('Второе число должно быть больше первого!')
        fin = None

for el in count(n):
    if el > fin:
        break
    else:
        print(el)

print('А теперь повторим список')

fin = None
while fin == None:
    text = input('Сколько букв отсыпать? ')
    fin = int(text) if text.isdigit() else None

с = 0
for el in cycle("ABC"):
    if с >= fin:
        break
    print(el)
    с += 1


