# Defining the decorator function
def counter(function):
    """"
    Decorator function where the closure will print
    the count of times the passed function has been called.
    """
    count = 0

    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{function.__name__} has been called {count} times")
        return function(*args, **kwargs)

    return inner


def add(x: int, y: int) -> int:
    """Returns the sum of the passed integers"""
    return x + y


# Implementing the decorator with traditional notation
add = counter(add)

print(f'"add" name after decoration: {add.__name__}')  # "inner" because of the closure
print(add.__code__.co_freevars)  # ('count', 'function')
print(add.__closure__)  # (cell, cell)
help(add)  # Metadata of "inner" because of the closure
print()


# Implementing the decorator with the @ notation
@counter
def sub(x: int, y: int) -> int:
    """Returns the substraction of the passed integers"""
    return x - y


print(f'"sub" name after decoration: {sub.__name__}')  # "inner" because of the closure
print(sub.__code__.co_freevars)
print(sub.__closure__)
print(sub.__annotations__)  # Annotations from "inner"
help(sub)  # Metadata of "inner" because of the closure
print()
