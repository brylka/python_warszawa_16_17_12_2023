class Person:
    def __init__(self, name, age):
        self.__name = name
        self._age = age
        self.__addAge()

    def __addAge(self):
        self._age += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

bartosz = Person("Bartosz", 44)

bartosz.__name = "Paweł"

#bartosz.__addAge()

print(bartosz._age)