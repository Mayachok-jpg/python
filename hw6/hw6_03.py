class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


crocodile = Position('Гена', 'Крокодил', 'крокодил в зоопарке', 90000, 30000)
postman = Position('Игорь Иванович', 'Печкин', 'почтальон', 38045, 696)

for pos in [crocodile, postman]:
    print('-'*50)
    print(f'{pos.name} {pos.surname}, работает на должности {pos.position} с окладом {pos._income["wage"]} и премией {pos._income["bonus"]}')
    print(f'Полное имя: {pos.get_full_name()}')
    print(f'Получает: {pos.get_total_income()}')

