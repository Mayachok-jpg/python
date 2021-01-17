words_string = []
statement = {}
try:
    with open('salary.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words = line.split()
            try:
                statement[words[0]] = int(words[1])
            except:
                print(f'Некорректные данные: {words}')
except FileNotFoundError:
    print ('Файл не существует')
except:
    print ('Что-то пошло не так')

print('Сотрудники с зарплатой меньше 20000: ')
for name in (statement):
    if statement[name] < 20000:
        print(name)
av_salary = sum(statement.values()) / len(statement)
print(f'Средняя зарплата сотрудика: {av_salary:2.2F}')

