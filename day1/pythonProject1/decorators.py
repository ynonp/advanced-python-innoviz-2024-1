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
def counting(real_twice):
    def twice(x: int) -> int:
        twice.call_count += 1
        # Before calling the decorated function ...
        result = real_twice(x)
        # After calling the decorated function ...
        # Modify the result value
        return result

    twice.call_count = 0
    return twice



# Same as doing: "twice = countig(twice)"
@counting
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

# How many times twice was called???
print(f"twice was called {twice.call_count} times")
print(f"thrice was called {thrice.call_count} times")









