all_sum = 0
ex = False

while ex == False:
    text_nums = (input ('Введите числа, разделенные пробелами: ')).split()
    num_list = []
    for num in text_nums:
        if num.lower() == 'q':
            ex = True
            print(f'Конец программы')
            break
        elif num.isdigit():
            num_list.append(int(num))
    all_sum += sum(num_list)
    print(f'Сумма чисел равна {all_sum}')