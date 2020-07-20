# Trying to resolve the problem with the original funtion metadata
# not working when function is wrapped in a decorator

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

    # Transferring the metadata of the function to the closure
    inner.__name__ = function.__name__
    inner.__doc__ = function.__doc__
    inner.__annotations__ = function.__annotations__
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
