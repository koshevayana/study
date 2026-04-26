import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.valid_w(width)
        self.valid_h(height)

    @classmethod
    def valid_w(cls, width):
        if width <= 0:
            raise ValueError ("Ширина должна быть положительным числом")

    @classmethod
    def valid_h(cls, height):
        if height <= 0:
            raise ValueError("Высота должна быть положительным числом")

    def get_width(self):
        return self.width

    def set_width(self, width):
        self.width = width
        self.valid_w(width)

    def get_height(self):
        return self.height

    def set_height(self, height):
        self.height = height
        self.valid_h(height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2*(self.width + self.height)

    def diagonal(self):
        return round(math.sqrt(self.width ** 2 + self.height ** 2), 2)

    def draw(self, char='*'):
            for i in range(self.width):
                for j in range(self.height):
                    print(char, end=' ')
                print()

rect=Rectangle(3,9)
print(rect.get_width())
print(rect.get_height())
print(rect.area())
print(rect.perimeter())
print(rect.diagonal())
rect.draw()


class Kg_to_ft:
    def __init__(self, kg):
        self.kg = kg
        self.valid_kg(kg)

    @classmethod
    def valid_kg(cls, kg):
        if not isinstance(kg,float) and not isinstance(kg,int):
            raise TypeError ("Килограммы задаются только числом")

    def get_kg(self):
        return self.kg
    def set_kg(self, kg):
        self.kg = kg

    def to_ft(self, suf=2.205):
        return self.kg*suf

kg1=Kg_to_ft(12)
kg2=Kg_to_ft(41)
kg3=Kg_to_ft("42")
print(kg1.to_ft())
print(kg2.to_ft())
print(kg3.to_ft())
