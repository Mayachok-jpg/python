class MyZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = 100
b = 0

try:
    if b == 0:
        raise MyZeroDivisionError('Зачем же делить на ноль?..')
    c = a/b
except MyZeroDivisionError as er:
    print('Свое исключение')
    print(er)
except ZeroDivisionError as er:
    # Сработает если не вызвать MyZeroDivisionError
    print('Обычное деление на ноль')
    print(er)
except Exception as er:
    # Если не указать явно, то свое в приоритете. Стандартное работат только если нет своего
    print('Другое исключение')
    print(er)





