import pytz
from datetime import datetime


# Function/Instance method to be added to a class
def current_object_info(self):
    """
    Returns a list containing a snapshot of the passed object.
    """
    results = []
    results.append(f"Time: {datetime.now(pytz.UTC)}")
    results.append(f"Class name: {self.__class__.__name__}")
    results.append(f"Memory address: {hex(id(self))}")
    values = {}
    for key, value in self.__dict__.items():
        values[key] = value
    results.append(values)
    return results


# Class decorator. Adds "current_object_info"
# as a new instance method in the passed class
def debug_info(cls):
    """
    Class decorator.
    Returns class with a new instance method that, when called, 
    returns a list with the current instance information.
    """
    cls.debug = current_object_info
    return cls


@debug_info
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person "{self.name}" is {self.age} years old'


@debug_info
class Car:
    def __init__(self, brand, model, year, top_speed: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._current_speed = 0

    @property
    def current_speed(self):
        return self._current_speed

    @current_speed.setter
    def current_speed(self, value):
        value = abs(value)
        if value < self.top_speed:
            self._current_speed = value
        else:
            raise ValueError("Current speed cannot be more than top speed")

    def __str__(self):
        return f'Car "{self.brand} {self.model} {self.year}"'


p1 = Person("Israel Mendoza", 28)
c1 = Car("Audi", "T", 2015, 250)
# Person and Car instances have the debug method
# because the class was monkey patched
person_info = p1.debug()
car_info = c1.debug()
print(person_info)
print(car_info)
