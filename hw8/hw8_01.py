class Data():

    def __init__(self, data_str):
        self.data_str = data_str

    @classmethod
    def to_int(cls, data_str):
        return list(map(int, data_str.split('-')))

    @staticmethod
    def valid(data_str):

        data_list = Data.to_int(data_str)

        if data_list[0] not in range(1, 32):
            print('День вне диапазона')
        if data_list[1] not in range(1, 13):
            print('Месяц вне диапазона')
        if data_list[2] not in range(1800, 3000):
            print('Год вне диапазона')


print(Data.to_int('1-12-1934'))
day = Data('3-12-1934')
print(day.to_int(day.data_str))
Data.valid('32-2-1934')
