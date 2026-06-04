class Line:
    def __init__(self, x1, y1, x2, y2, color, width):
        if not all(isinstance(coord, int) for coord in [x1, y1, x2, y2]):
            raise TypeError("Координаты должны быть целочисленными")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.width = width

    def draw(self):
        print(f"Рисование линии: ({self.x1}, {self.y1}), ({self.x2}, {self.y2}), {self.color}, {self.width}")


class Rect:
    def __init__(self, x1, y1, x2, y2, color, width):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.width = width

    def draw(self):
        print(f"Рисование прямоугольника: ({self.x1}, {self.y1}), ({self.x2}, {self.y2}), {self.color}, {self.width}")


line1 = Line(1, 2, 10, 20, "red", 1)
line1.draw()

try:
    line2 = Line(10.2, 20, 100, 200, "green", 3)
except TypeError as e:
    print(f"Ошибка: {e}")
    print("Координаты должны быть целочисленными")

rect1 = Rect(7, 9, 12, 15, "red", 1)
rect1.draw()

rect2 = Rect(30.5, 40.2, 50, 60, "red", 1)
rect2.draw()