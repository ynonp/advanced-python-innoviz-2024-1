"""
1. While writing my code I'll use type hints
2. Debug using pycharm
3. Write tests for small chunks of code
"""


def fib(n: int) -> int:
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def twice(x: int|str) -> int:
    return x * 2


print(twice("hello"))
print(fib(5))
