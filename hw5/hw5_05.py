from random import randint

with open('hw5_05.txt', 'w', encoding='utf-8') as f:
    for i in range(10):
        f.write(f'{str(randint(0, 100))} ')

with open('hw5_05_res.txt', 'r', encoding='utf-8') as f:
    nums_text = f.read().split()

nums = [int(num) for num in nums_text]
print(f'Сумма чисел в файле {sum(nums)}')

