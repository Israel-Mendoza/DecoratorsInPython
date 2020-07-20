from functools import wraps


def counter(function):
    """"
    Decorator function where the closure will print
    the count of times the passed function has been called.
    """
    count = 0

    # @wraps(function)    <- Alternative notation to line 19
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{function.__name__} has been called {count} times")
        return function(*args, **kwargs)

    # Transferring the metadata of the function to the closure
    inner = wraps(function)(inner)
    return inner


@counter
def add(x: int, y: int) -> int:
    """Returns the sum of the passed integers"""
    return x + y


print(f'"add" name after decoration: {add.__name__}')  # Correct name
print(add.__code__.co_freevars)
print(add.__closure__)
print(add.__annotations__)  # Correct annotations
help(add)  # Correct documentation, WRONG function signature
print()
