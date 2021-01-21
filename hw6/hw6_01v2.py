from time import sleep
from termcolor import colored


class TrafficLight():
    __color = 'green'
    __colors = ['red', 'yellow', 'green']

    def running(self):
        self.next_color('red', 7)
        self.next_color('yellow', 2)
        self.next_color('green', 1)

    def next_color(self, color, ctime):
        i = self.__colors.index(color)
        if self.__colors[i - 1] != self.__color:
            raise ValueError("Неправильный режим")
        self.__color = color
        print(colored(self.__color, self.__color))
        sleep(ctime)


traffic_light = TrafficLight()

try:
    traffic_light.running()
except:
    print('Светофор сломался')

print('Программа завершена')
