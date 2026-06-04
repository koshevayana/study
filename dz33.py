from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, side, color):
        self.side = side
        self.color = color

    def perimeter(self):
        return self.side * 4

    def area(self):
        return self.side ** 2

    def draw(self):
        print("***")
        print("***")
        print("***")
        print("***")

    def info(self):
        print("Квадрат")
        print(f"Сторона: {self.side}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()


class Rectangle(Shape):
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self.color = color

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width

    def draw(self):
        print("******")
        print("******")
        print("******")

    def info(self):
        print("Прямоугольник")
        print(f"Длина: {self.length}")
        print(f"Ширина: {self.width}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()


class Triangle(Shape):
    def __init__(self, side1, side2, side3, color):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.color = color

    def perimeter(self):
        return self.side1 + self.side2 + self.side3

    def area(self):
        s = self.perimeter() / 2
        return round(math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3)), 2)

    def draw(self):
        print("*")
        print("***")
        print("*****")
        print("*******")
        print("*********")
        print("***********")
        print("*************")

    def info(self):
        print("Треугольник")
        print(f"Сторона 1: {self.side1}")
        print(f"Сторона 2: {self.side2}")
        print(f"Сторона 3: {self.side3}")
        print(f"Цвет: {self.color}")
        print(f"Площадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")
        self.draw()


square = Square(3, "red")
rectangle = Rectangle(3, 7, "green")
triangle = Triangle(11, 6, 6, "yellow")

square.info()
print()
rectangle.info()
print()
triangle.info()