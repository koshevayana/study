class Liquid:
    def __init__(self, name, density):
        self.name = name
        self.density = density

    def change_density(self, new_density):
        self.density = new_density

    def calculate_volume(self, mass):
        return mass / self.density

    def calculate_mass(self, volume):
        return volume * self.density

    def display_info(self):
        print(f"Жидкость: {self.name}")
        print(f"Плотность: {self.density} kg/m3")


class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength

    def change_strength(self, new_strength):
        self.strength = new_strength

    def display_info(self):
        super().display_info()
        print(f"Крепость: {self.strength}%")


wine = Liquid("Wine", 1000)
wine.display_info()
print()

mass = wine.calculate_mass(0.5)
print(f"Вес 0.5 m3 of Wine составляет {mass:.1f} кг")

volume = wine.calculate_volume(300)
print(f"Объем 300 кг Wine равен {volume:.1f} m3")