from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, title):
        self.title = title

    @property
    def fabric_consumpion(self):
        pass


class Coat(Clothes):

    def __init__(self, title, size):
        Clothes.__init__(self, title)
        self.size = size

    @property
    def fabric_consumpion(self):
        return round(self.size / 6.5 + 0.5, 2)


class Suit(Clothes):

    def __init__(self, title, height):
        Clothes.__init__(self, title)
        self.height = height

    @property
    def fabric_consumpion(self):
        return round(self.height * 2 + 0.3, 2)


coat = Coat('черное пальто', 8)
suit = Suit('Полосатый костюм', 2.05)

print(coat.title)
print(coat.fabric_consumpion)

print(suit.title)
print(suit.fabric_consumpion)

print(f'Общий расход ткани {round(suit.fabric_consumpion + coat.fabric_consumpion, 2)} метров')
