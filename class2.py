class Person:
    def __init__(self, name, x, nr=0):
        self.name = name
        self.age = x
        self.serial_number = nr
    def hello(self):
        print(f"Nazywam się {self.name} i mam {self.age} lat oraz numer seryjny {self.serial_number}.")

    def __str__(self):
        return f"Obiekt z klasy Person o nazwie: {self.name}, wieku: {self.age}, numerze seryjnym: {self.serial_number}"


bartosz = Person("Bartosz",44)
#bartosz.hello()

print(bartosz)

