class Person:
    def __init__(self, name, x, nr):
        #self.name = "Paweł"
        self.name = name
        self.age = x
        self.serial_number = nr
    def hello(self):
        #print("Nazywam się " + self.name + " i mam " + str(self.age), end="\n")
        #print("Nazywam się", self.name, "i mam", self.age, sep="!", end="\n")
        print(f"Nazywam się {self.name} i mam {self.age} lat oraz numer seryjny {self.serial_number}.")

    def __str__(self):
        return f"Obiekt z klasy Person o nazwie: {self.name}, wieku: {self.age}, numerze seryjnym: {self.serial_number}"

#Person().hello()

bartosz = []
        # [0,1,2,3,4,5,6,7,8,9]
        # [10,12,14,16,18,20]
lista = [10,12,14,16,18,20]
for i in lista:

    bartosz2 = Person("Bartosz", 40, i)
    bartosz.append(bartosz2)


#bartosz[1].hello()

#for person in bartosz:
    #person.hello()

#bartosz[3].hello()

print(bartosz)
print(bartosz[0])