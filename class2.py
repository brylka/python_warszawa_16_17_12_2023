class Person:
    def __init__(self, name, x, nr=0):
        self.name = name
        self.age = x
        self.serial_number = nr
    def hello(self, password=''):
        if password == '':
            print("Podaj hasło!")
        elif password == 'qwer1234':
            print(f"Nazywam się {self.name} i mam {self.age} lat oraz numer seryjny {self.serial_number}.")
        else:
            print("Hasło niepoprawne!")

    def __str__(self):
        return f"Obiekt z klasy Person o nazwie: {self.name}, wieku: {self.age}, numerze seryjnym: {self.serial_number}"

    def __del__(self):
        print("Ubili mnie!")

bartosz = Person("Bartosz",44)
bartosz.hello('qwer1234')

print(bartosz)

del bartosz

