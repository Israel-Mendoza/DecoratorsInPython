from fractions import Fraction


def add_instance_method(cls):
    # Adds an instance method to the passed class (monkey patching)
    cls.speak = lambda self, message: f'{self.__class__.__name__} says "{message}"'
    return cls


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


# Decorating the existant class
Fraction = add_instance_method(Fraction)
Person = add_instance_method(Person)
f1 = Fraction(8 / 4)
p1 = Person("Israel Mendoza", 28)

print(f1.speak("soy una puta fracción"))
print(p1.speak("no soy nada"))
