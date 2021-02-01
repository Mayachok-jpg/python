class ComplexNumber():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}+{self.b}i'

    def __add__(self, other):
        if type(other) != ComplexNumber:
            raise ValueError
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        if type(other) != ComplexNumber:
            raise ValueError
        return ComplexNumber(self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b)


cn1 = ComplexNumber(1, 3)
cn2 = ComplexNumber(6, 3)

x = complex(1, 3)
y = complex(6, 3)

print(f'Мое число: {cn1}, встроеное: {x}')
print(f'Мое число: {cn2}, встроенное: {y}')
print(f'Мое сложение: {cn2 + cn1}, встроенное: {y+x}')
print(f'Мое умножение: {cn1 * cn2}, встроенное: {x * y}')
