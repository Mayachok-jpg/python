lessons = {}

with open('hw5_06.txt', 'r', encoding='utf-8') as f:
    for line in f:
        subject = line.split()
        hours = 0
        try:
            for i in range(1, 4):
                if subject[i] != '—':
                    hours += int(subject[i].split('(')[0])
            lessons[subject[0].rstrip(':')] = hours
        except:
            print('Некорректные данные')

print(lessons)
