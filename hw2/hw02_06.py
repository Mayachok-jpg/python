# Реализовать структуру данных «Товары»
data = [] #список кортежей
analit = {}
menu = '1. Ввести данные\n2. Вывести данные\n3. Аналитика\n4. Выход'
while True:

    print(menu)
    change = input('Выберите пункт меню: ')

    if change == '1':
        ware = input('Введите информацию о товаре (название, цена, количество, единицы измерения) через пробел: ').split()
        ware_db = {
            'Название товара' : ware[0],
            'цена' : int(ware[1]),
            'количество': int(ware[2]),
            'ед.' : ware[3],

        }
        data.append((len(data) + 1, ware_db))

    elif change == '2':
        for el in data:
            print(el)

    elif change == '3':
        names = []
        costs = []
        counts = []
        units = []

        for el in data:
            names.append(el[1]['Название товара'])
            costs.append(el[1]['цена'])
            counts.append(el[1]['количество'])
            units.append(el[1]['ед.'])
        analit['Название товара'] = list(set(names))
        analit['цена'] = list(set(costs))
        analit['количество'] = list(set(counts))
        analit['ед.'] = list(set(units))
        print(analit)

    elif change == '4':
        break

    else:
        print('Повторите ввод!')
