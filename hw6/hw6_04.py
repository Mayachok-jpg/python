from random import randint, choice


class Car():
    def __init__(self, color, name, is_police):
        self.speed = 0
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed = randint(1, 100)
        print(f'{self.name}: поехала.')

    def stop(self):
        self.speed = 0
        print(f'{self.name}: машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: машина повернула {direction}')

    def show_speed(self):
        print(f'Текущая скорость {self.speed}')


class TownCar(Car):
    def __init__(self, color, name, is_police=False):
        Car.__init__(self, color, name, is_police)

    def show_speed(self):
        mes = f'Скорость машины {self.speed}' if self.speed < 60 else f'Скорость машины {self.speed}. Превышение скорости на {self.speed - 60}'
        print(mes)


class SportCar(Car):
    def __init__(self, color, name, is_police=False):
        Car.__init__(self, color, name, is_police)


class WorkCar(Car):
    def __init__(self, color, name, is_police=False):
        Car.__init__(self, color, name, is_police)

    def show_speed(self):
        mes = f'Скорость машины {self.speed}' if self.speed < 40 else f'Скорость машины {self.speed}. Превышение скорости на {self.speed - 40}'
        print(mes)


class PoliceCar(Car):
    def __init__(self, color, name, is_police=True):
        Car.__init__(self, color, name, is_police)


town_car = TownCar('белая', 'Corolla')
sport_car = SportCar('красная', 'Lamborghini')
work_car = WorkCar('желтая', 'Caterpillar 797')
police_car = PoliceCar('Черная', 'Ford Fairlane Crown Victoria')

cars = [town_car, sport_car, work_car, police_car]

for car in cars:

    if car.is_police:
        print('Полиция!')

    print(f'{car.name}, {car.color}')

    r = randint(1, 3)
    if r == 1:
        car.go(),
    elif r == 2:
        car.stop(),
    else:
        car.turn(choice(('направо', 'налево', 'назад')))

    car.show_speed()
    print('-' * 100)
