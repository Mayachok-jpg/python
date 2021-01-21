from time import sleep
from termcolor import colored


class TrafficLight():
    __color = {'red': 7, 'yellow': 2, 'green': 5}

    def running(self):
        for color in self.__color:
            print(colored(color, color))
            sleep(self.__color[color])

trafficlight = TrafficLight()
trafficlight.running()
print('Программа завершена')


