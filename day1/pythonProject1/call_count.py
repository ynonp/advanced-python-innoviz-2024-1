from functools import lru_cache
from collections import defaultdict
class Counter:
    def __init__(self):
        self.value = 0

    def inc(self):
        self.value += 1



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

def counting_v2(counter):
    def decorator(f):
        def inner(x: int) -> int:
            print(inner)
            counter.inc()
            # Before calling the decorated function ...
            result = f(x)
            # After calling the decorated function ...
            # Modify the result value
            return result

        return inner
    return decorator

twice_counter = Counter()
@lru_cache()
@counting_v2(twice_counter)
def twice(x):
    print(f"twice::{x}")
    return x * 2


twice(10)
twice(10)
twice(10)
twice(10)

print(twice_counter.value)

