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
