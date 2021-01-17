with open('hw5_01.txt', 'w', encoding='utf-8') as f:
    text = ' '
    while text != '':
        text = input('Введите данные: ')
        f.write(f'{text}\n')


# f = open('hw5_01.txt', 'w')
# text = ' '
# while text != '':
#     text = input('Введите данные: ')
#     f.write(f'{text}\n')
# f.close()
