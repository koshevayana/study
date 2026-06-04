class Student:
    def __init__(self, name, model, processor, ram):
        self.name = name
        self.model = model
        self.processor = processor
        self.ram = ram

    def info(self):
        print(f"{self.name} => {self.model}, {self.processor}, {self.ram}")


s1 = Student("Roman", "HP", "i7", "16")
s2 = Student("Vladimir", "HP", "i7", "16")

s1.info()
s2.info()