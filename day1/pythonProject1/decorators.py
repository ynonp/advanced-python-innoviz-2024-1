# Python3

def counter():
    count = 0
    def f():
        nonlocal count
        count += 1
        print(count)
    return f


c = counter()
c()
c()

d = counter()
c()
d()

# ----------------------------


"""
In python we can add "properties" to anything
"""
def counting(f):
    def inner(x: int) -> int:
        inner.call_count += 1
        # Before calling the decorated function ...
        result = f(x)
        # After calling the decorated function ...
        # Modify the result value
        return result

    inner.call_count = 0
    return inner


def counting_in_twos(f):
    def inner(x: int) -> int:
        inner.call_count += 2
        # Before calling the decorated function ...
        result = f(x)
        # After calling the decorated function ...
        # Modify the result value
        return result

    inner.call_count = 0
    return inner



def max5(f):
    call_count = 0
    def inner(x: int) -> int:
        nonlocal call_count
        call_count += 1
        if call_count > 5:
            raise Exception("Called too many times")

        result = f(x)
        return result

    return inner


def memoized(f):
    memory = {}

    def inner(n: int):
        if n not in memory:
            # memory.__setattr__(n, f(n))
            memory[n] = f(n)
        return memory[n]

    return inner





# Same as doing: "twice = countig(twice)"
@max5
def twice(x: int) -> int:
    return x * 2

# Same as doing: "thrice = countig(thrice)"
@counting
def thrice(x: int) -> int:
    return x * 3


thrice(2)
thrice(5)

twice(10)
twice(20)
twice(30)

@memoized
def fib(n):
    print(f"Calculating fib({n})")
    if n < 2:
        return 1
    return fib(n-1) + fib(n-2)


fib(10)






@memoized
def square(x):
    print(f"Calling square({x})")
    return x * x


print(square(10))
print(square(10))
print(square(10))
print(square(10))







# How many times twice was called???
# print(f"twice was called {twice.call_count} times")
# print(f"thrice was called {thrice.call_count} times")









