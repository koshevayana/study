class Book:
    def __init__(self, name, year, izd, author, price):
        self.name = name
        self.year = year
        self.izd = izd
        self.author = author
        self.price = price
    def get_name(self):
        return self.name
    def set_name(self, name):
        self.name = name
    def get_year(self):
        return self.year
    def set_year(self, year):
        self.year = year
    def get_izd(self):
        return self.izd
    def set_izd(self, izd):
        self.izd = izd
    def get_author(self):
        return self.author
    def set_author(self, author):
        self.author = author
    def get_price(self):
        return self.price
    def set_price(self, price):
        self.price = price
    def print_info(self):
        print(f"'{self.name}' - {self.author} ({self.year}, издательство {self.izd}) - {self.price} руб.")

b1=Book ('Мастер и Маргарита', 1967, 'Эксмо', 'Булгаков', 700)

b1.print_info()