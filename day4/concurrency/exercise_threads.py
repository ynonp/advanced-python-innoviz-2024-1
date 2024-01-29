import math


def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

"""
Your task:
Count how many prime numbers there are between
1 and 1_000_000
Use:
    1. Single thread
    2. multiprocessing.dummy
    3. multiprocessing

Print the time it took and the results    
"""
