words_string = []
try:
    with open('file.txt', 'r', encoding='utf-8') as f:
        for line in f:
            words = line.split()
            words_string.append(len(words))
except FileNotFoundError:
    print ('Файл не существует')
except:
    print ('Что-то пошло не так')

for i, el in enumerate(words_string):
    print(f'В {i+1} строке {el} слов')
