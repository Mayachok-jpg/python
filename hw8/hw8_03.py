class NotANumber(Exception):
    def __init__(self, *arg):
        self.value = arg[0]

    def __str__(self):
        return f'В список можно добавлять только числа. "{self.value}" — не число'


def is_digit(n):
    try:
        int(n)
        return True
    except:
        return False


res_list = []

print('Вводите числа — элементы списка. Для окончания нажмите "q"')

while True:
    el = input('Введите элемент списка: ')
    if el == 'q':
        break
    else:
        try:
            if is_digit(el):
                res_list.append(int(el))
            else:
                raise NotANumber(el)
        except NotANumber as er:
            print(er)

print(f'Полученный список: {res_list}')
