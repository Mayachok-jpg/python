# Реализовать функцию, принимающую несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def about_user(name, surname, birth_year, city, email, phone):
    print(' '.join([name, surname, birth_year, city, email, phone]))

about_user(name = input('Введите имя пользователя: '),
            surname = input('Введите фамилию: '),
            birth_year = input('Введите год рождения: '),
            city = input('Введите город проживания: '),
            email = input('Введите e-mail: '),
            phone = input('Введите phone: '))
