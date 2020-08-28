def debug_info(a_list):
    """
    Decorator factory. Accepts an empty list, which will
    be populated with the object snapshots.
    """
    import pytz
    from datetime import datetime

    def _debug_info(cls):
        """
        Returns a class decorator, which returns class with a 
        new instance method called "debug" that, when called, 
        returns a list containing the instance's snapshot.
        """
        def inner(self):
            """
            Appends the instance snapshot to the "a_list" free variable.
            """
            results = []
            results.append(f"Time: {datetime.now(pytz.UTC)}")
            results.append(f"Class name: {self.__class__.__name__}")
            results.append(f"Memory address: {hex(id(self))}")
            values = {}
            for key, value in self.__dict__.items():
                values[key] = value
            results.append(values)
            a_list.append(results)

        cls.debug = inner
        return cls

    return _debug_info


# Empty list, which will store the instances' snapshots.
my_results = list()


@debug_info(my_results)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'Person "{self.name}" is {self.age} years old'


@debug_info(my_results)
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


p1 = Person("Israel", 28)
c1 = Car("Audi", "T", 2015, 250)

# Person and Car instances have the debug method
# because the class was monkey patched via a decorator
p1.debug()
c1.debug()

for result in my_results:
    print(result)
