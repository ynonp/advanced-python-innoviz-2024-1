import itertools

def fib():
    a, b = 1, 1

    while True:
        # 1   1  [3   5]   8   13   21
        a, b = b, a + b
        yield a

for i in itertools.takewhile(lambda x: x < 100, fib()):
    print(i)

print(sum(itertools.islice(fib(), 100)))

print(next(itertools.islice(fib(), 4, 5)))

# Infinite loop
# for i in fib():
#     print(i)
