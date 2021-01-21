class Road():

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def asp_mass(self, asp_mass_m, thick):
        return self._length * self._width * asp_mass_m * thick/1000


grandmother_road = Road(5000, 20)

print(f'Асфальта понадобится {grandmother_road.asp_mass(25, 5):.2f} т')

