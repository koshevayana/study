class Point3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __getitem__(self, key):
        if key == "x":
            return self.x
        if key == "y":
            return self.y
        if key == "z":
            return self.z
        raise KeyError(f"Недопустимый ключ: {key}")

    def __setitem__(self, key, value):
        if key == "x":
            self.x = value
        elif key == "y":
            self.y = value
        elif key == "z":
            self.z = value
        else:
            raise KeyError(f"Недопустимый ключ: {key}")

    def __add__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
        raise TypeError(f"Неподдерживаемый тип операнда для +: Point3D и {type(other).__name__}")

    def __sub__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
        raise TypeError(f"Неподдерживаемый тип операнда для -: Point3D и {type(other).__name__}")

    def multiply(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)
        raise TypeError(f"Неподдерживаемый тип операнда для умножения: Point3D и {type(other).__name__}")

    def divide(self, other):
        if isinstance(other, Point3D):
            if other.x == 0 or other.y == 0 or other.z == 0:
                raise ZeroDivisionError("Деление на ноль")
            return Point3D(int(self.x / other.x), int(self.y / other.y), int(self.z / other.z))
        raise TypeError(f"Неподдерживаемый тип операнда для деления: Point3D и {type(other).__name__}")

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"


p1 = Point3D(12, 15, 18)
p2 = Point3D(6, 3, 9)

print("Координаты 1-й точки:", p1)
print("Координаты 2-й точки:", p2)

p_add = p1 + p2
print("Сложение координат:", p_add)

p_sub = p1 - p2
print("Вычитание координат:", p_sub)

p_mul = p1.multiply(p2)
print("Умножение:", p_mul)

p_div = p1.divide(p2)
print("Деление:", p_div)

print("Равенство координат:", p1 == p2)

print("x =", p1["x"])
print("x1 =", p2["x"])
print("y =", p1["y"])
print("y1 =", p2["y"])
print("x =", p1["x"])
print("z1 =", p2["z"])

p1["x"] = 20
print("Запись значения в координату x:", p1["x"])