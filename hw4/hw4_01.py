from sys import argv

script_name, hours, rate, bonus = argv

try:
    salary = int(hours)*int(rate) + int(bonus)
    print("Зарплата: ", salary)
except:
    print('Что-то пошло не так')


