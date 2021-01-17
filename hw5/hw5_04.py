nums = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
       }
try:
    with open('nums.txt', 'r', encoding='utf-8') as f, open('nums_res.txt', 'w', encoding='utf-8') as f_res:
        for line in f:
            word = line.split()
            new_line = line.replace(word[0], nums[word[0]])
            f_res.write(new_line)
except:
    print('Что-то пошло не так')
