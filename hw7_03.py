class Unit():

    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        if type(other) == type(self):
            return Unit(self.cell + other.cell)
        else:
            raise ValueError

    def __sub__(self, other):
        if type(other) == type(self) and self.cell - other.cell > 0:
            return Unit(self.cell - other.cell)
        else:
            raise ValueError

    def __mul__(self, other):
        if type(other) == type(self):
            return Unit(self.cell * other.cell)
        else:
            raise ValueError

    def __truediv__(self, other):
        if type(other) == type(self):
            return Unit(round(self.cell / other.cell))
        else:
            raise ValueError

    def make_order(self, n):
        nstr = self.cell // n
        lstr = self.cell % n
        return ('*' * n + '\n') * nstr + '*' * lstr


unit1 = Unit(3)
unit2 = Unit(4)

unit3 = unit1 + unit2
unit4 = unit2 - unit1
unit5 = unit2 * unit1
unit6 = unit2 / unit1
unit7 = Unit(103)

for u in [unit1, unit2, unit3, unit4, unit5, unit6]:
    print(f'{u.cell}')

print(unit5.make_order(5))
print(unit7.make_order(20))
