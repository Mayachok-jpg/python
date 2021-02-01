class Storage():

    def __init__(self):
        self.list_of_office_equipment = []

    def __str__(self):
        res = 'В наличии:\n'
        for el in self.list_of_office_equipment:
            res += f"{el['Тип']}, {el['Где находится']}, в количестве {el['Количество']}\n"
        return 'склад пуст' if res == 'В наличии:\n' else res

    def add_to_storage(self, office_equipment, num):
        self.ship_to_department(office_equipment, 'склад', num)

    def add_office_equipment(self, type_of_equipment):
        ware = input(type_of_equipment.add_text).split()
        while len(ware) == 0:
            ware = input('Необходимо ввести название (модель, тип): ').split()
        if len(ware) < 3:
            for n in range(len(ware) - 1, 2):
                ware.append('')
        equipment = type_of_equipment(ware[0], ware[1], ware[2])
        print(equipment)
        num = input('Cколько их: ')
        while not Storage.valid_num(num):
            num = input('Cколько их: ')
        loc = input('Куда направить: ')
        storage.ship_to_department(equipment, loc, int(num))

    @property
    def what_is_storage(self):
        print(self)

    def ship_to_department(self, office_equipment, department, num :int):
        location = {}
        location['Тип'] = office_equipment
        location['Где находится'] = department
        location['Количество'] = num
        added = False
        for el in self.list_of_office_equipment:
            if el['Тип'] == office_equipment and el['Где находится'] == department:
                el['Количество'] += num
                added = True
                # print('Уже было, добавили')
                break
        if not added:
            self.list_of_office_equipment.append(location)
            # print('Не было, отправили')

    @staticmethod
    def valid_num(n):
        if n.isdigit() and int(n) > 0:
            return True
        else:
            print('Количество должно быть целым положительным числом!')
            return False


class OfficeEquipment():

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def __str__(self):
        return f'{self.name}, модель {self.model}'

class Printer(OfficeEquipment):
    add_text = 'Введите информацию о принтере (название, модель, тип печати) через пробел: '
    def __init__(self, name, model, print_type):
        OfficeEquipment.__init__(self, name, model)
        self.print_type = print_type


class Scanner(OfficeEquipment):
    add_text = 'Введите информацию о сканере (название, модель, тип) через пробел: '
    def __init__(self, name, model, scanner_type):
        OfficeEquipment.__init__(self, name, model)
        self.scanner_type = scanner_type


storage = Storage()
print(storage)
printer = Printer('Лазерджет', '340j', 'лезерный')
printer2 = Printer('Лазерджет', '3', 'лазерный')
scanner = Scanner('Asap', '810i', 'портативный')
storage.add_to_storage(printer, 3)
storage.add_to_storage(printer2, 5)
print(storage)
storage.add_to_storage(scanner, 6)
print(storage)
storage.ship_to_department(printer, 'креативный отдел', 2)
print(storage)
print('—' * 30)

menu = '1. Добавить технику\n2. Инвентаризация\n3. Выдать технику\n4. Выход\n'
menu1 = '\n1. Добавить сканер\n2. Добавить принтер\n3. Отмена'

while True:
    print(menu)
    change = input('Выберите пункт меню: ')

    if change == '1':

        print(menu1)
        change1 = input('Выберите пункт меню: ')

        if change1 == '1':
            storage.add_office_equipment(Scanner)

        if change1 == '2':
            storage.add_office_equipment(Printer)

        if change1 == '3':
            print(menu)
            change = input('Выберите пункт меню: ')

    if change == '2':
        print(f'\n{"—" * 30}')
        print(storage)
        print(f'\n{"—" * 30}')

    if change == '3':
        print(f'\n{storage}')
        extradited = False
        name = input('Что выдаем? ')
        for el in storage.list_of_office_equipment:
            if el['Тип'].name == name and el['Где находится'] == 'склад':
                num = input('Сколько? ')
                while not Storage.valid_num(num):
                    num = input('Cколько их: ')
                num = int(num)
                if num > el['Количество']:
                    num = el['Количество']
                    print(f'Столько нет, есть только {el["Количество"]}')
                loc = input('Куда передаем? ')
                el['Количество'] -= num
                storage.ship_to_department(el['Тип'], loc, num)
                print(f'Отправили: {el["Тип"]}, {num}, {loc}')
                storage.list_of_office_equipment = [el for el in storage.list_of_office_equipment if el['Количество'] != 0]
                extradited = True
                break

        if not extradited:
            print('Такого на складе не нашлось\n')

    if change == '4':
        break
