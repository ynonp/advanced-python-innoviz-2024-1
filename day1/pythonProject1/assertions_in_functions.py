"""
Disadvantage of assertions:
It can limit your ability to use the code in creative ways
"""
from typing import Sized

def longer_than(n: int, items: list[Sized]):
    return [i for i in items if len(i) > n]


print(longer_than(5, ["a", "b", "hello", "four and five"]))
print(longer_than(5, [range(2), range(10), range(100)]))
