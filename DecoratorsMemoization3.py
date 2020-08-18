from functools import lru_cache

# lru_cache takes in the max_cache_value
# It is nothing more than a memoization decorator


@lru_cache(8)
def fibonacci(n):
    print(f"Calculating {n}!")
    return 1 if n < 3 else fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci(8))
print(fibonacci(15))
