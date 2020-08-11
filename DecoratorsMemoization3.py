from functools import lru_cache


@lru_cache(maxsize=8)
def fibonacci(n):
    print(f"Calculating {n}!")
    return 1 if n < 3 else fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci(8))
print(fibonacci(15))
