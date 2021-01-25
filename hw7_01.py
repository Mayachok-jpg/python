class Matrix():
    def __init__(self, ll):
        self.nums = ll

    def __str__(self):

        max_len = len(str(max(map(max, self.nums))))
        # 1 попытка
        # res = ''
        # for el_str in self.nums:
        #     for el_st in el_str:
        #         res += f'{el_st:^{max_len}} '
        #     res += '\n'
        # return res[:-2]

        # Вторая попытка
        return str('\n'.join([' '.join([f'{str(j):^{max_len}}' for j in i]) for i in self.nums]))

    def __add__(self, other):

        # 1 попытка
        # if type(other) == Matrix and len(self.nums) == len(other.nums):
        #     for i, el_str in enumerate(self.nums):
        #         if len(el_str) == len(other.nums[i]):
        #             new_m = []
        #             for i, el_s in enumerate(self.nums):
        #                 new_str = list(map(lambda x, y: x + y, el_s, other.nums[i]))
        #                 new_m.append(new_str)
        #         else: raise ValueError
        # else:
        #     raise ValueError
        # return Matrix(new_m)

        # Вторая попытка
        if type(other) == Matrix and [len(el1) for el1 in self.nums] == [len(el2) for el2 in other.nums]:
            return Matrix([[el_1 + el_2 for el_1, el_2 in zip(self.nums[i], other.nums[i])]
                           for i in range(len(self.nums))])
        else:
            raise ValueError


m = Matrix([[10, 2, 3, 0], [5, 6, 7, 80], [6, 7, 9, 0]])
m2 = Matrix([[0, 2, 3, 4], [1, 1, 1, 1], [1, 1, 3, 1]])
m4 = Matrix([[0, 2, 3, 4], [1, 1, 1, 1]])

print(m)
print('+')
print(m2)
print('=')
print(m+m2)

try:
    m5 = m4 + m2
except:
    print(('Размер матриц не совпадает'))


