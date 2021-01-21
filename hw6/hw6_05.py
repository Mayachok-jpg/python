class Stationery:
    def __init__(self, name):
        self.title = name

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def __init__(self, name, color):
        Stationery.__init__(self, name)
        self.color = color

    def draw(self):
        print('Рисуем ручкой')


class Pencil(Stationery):

    def draw(self):
        print('Рисуем карандашом')


class Handle(Stationery):

    def draw(self):
        print('Рисуем маркером')


chalk = Stationery('Мел')
pen = Pen('Черная ручка', 'черная')
pencil = Pencil('Короткий карандаш')
handle = Handle('Маркер')

stats = [pen, chalk, pencil, handle]
for stat in stats:
    print(f'{stat.title}:', end=' ')
    stat.draw()
