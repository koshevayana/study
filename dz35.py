class PositiveInt:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        return obj.__dict__.get(self.name, 0)

    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} должно быть целым числом")
        if value <= 0:
            raise ValueError(f"{self.name} должно быть положительным числом")
        obj.__dict__[self.name] = value


class Triangle:
    a = PositiveInt()
    b = PositiveInt()
    c = PositiveInt()

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def exists(self):
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return True
        return False

    def __str__(self):
        if self.exists():
            return f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) существует."
        else:
            return f"Треугольник со сторонами ({self.a}, {self.b}, {self.c}) не существует."


t1 = Triangle(2, 5, 6)
t2 = Triangle(5, 2, 8)
t3 = Triangle(7, 3, 6)

print(t1)
print(t2)
print(t3)