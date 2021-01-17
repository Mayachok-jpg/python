import json

profit_dict = {}
av_profit_dict = {}
firm_list = []
sum_profit = 0
n = 0

with open('hw5_07.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        firm_list = line.split()
        try:
            firm_profit = int(firm_list[2]) - int(firm_list[3])
            profit_dict[firm_list[0]] = firm_profit
        except:
            print('Некорректные данные')
for prof in profit_dict:
    if profit_dict[prof] > 0:
        sum_profit += profit_dict[prof]
        n += 1
try:
    av_profit_dict['average_profit'] = round(sum_profit/n, 2)
except ZeroDivisionError:
    print('Ни у кого нет прибыли')
firm_list = [profit_dict, av_profit_dict]
print(f'Результат: {firm_list}')

with open("hw5_07.json", "w") as j_f:
    json.dump(firm_list, j_f)

with open("hw5_07.json", "r") as j_f:
    res = json.load(j_f)
    print(f'Извлекаем из файла: {res}')

