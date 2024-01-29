"""
Type Hints are a tool we use to detect problems in our code
related to types
"""


"""
This code doesn't tell us what type of input it expects
"""

# Use a type - easy
def twice(x: int) -> int:
    return x * 2


# Use multiple types - still easy
def twice_v2(x: int|str) -> int|str:
    return x * 2


# Use collections - still easy
def longer_than(n: int, items: list[str]) -> list[str]:
    return [i for i in items if len(i) > n]


"""
Coffee + Lab

1. Find in your project a function that you can extract
from your code and copy to our lab

2. Copy it to a new lab project, and run it

3. Add type hints to that function

I need a type hint for "something that is ????????"
typing.Callable

I need a function that takes a str and returns (float, float),
but could also return None

"""

from typing import Optional, Sized, Callable, TypeVar, Iterable, Sequence, MutableSequence

# f is a function taking a single int and returning an int value
def my_map(f: Callable[[int], int], items: list[int]) -> list[int]:
    return list(map(f, items))


T = TypeVar("T", bound=Sized)
def longer_than_v2(n: int, items: Sequence[T]) -> Sequence[T]:
    items[0] = "yay"
    return [i for i in items if len(i) > n]


long_strings = longer_than_v2(4, ["a", "b", "abcdefg"])
if long_strings[0].startswith('a'):
    print("the first long string starts with an a")


long_strings = longer_than_v2(4, [range(10), range(20)])
if long_strings[0].startswith('a'):
    print("the first long string starts with an a")






longer_than_v2(10, ["one", range(100), "two and three"])



def get_video_properties(video: str) -> Optional[tuple[float, float]]:
    if video.startswith("a"):
        return (200, 300)
    return None


x = get_video_properties("wow")
if x is not None:
    print(x[0])
