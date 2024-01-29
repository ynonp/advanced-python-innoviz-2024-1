"""
multiprocessing.dummy is a thread based implementation of multiprocessing module
and provides threads based constructs for doing things in parallel
"""

import multiprocessing as mp
import time

def f(x):
    return x*x

# Time with multiprocessing.dummy 895642000
# Time with single thread         742197000
# Time with multiprocessing      1026566000

if __name__ == '__main__':
    start = time.time_ns()
    # print(sum(f(i) for i in range(10_000_000)))

    with mp.Pool(5) as p:
        print(sum(p.map(f, range(10_000_000))))
    end = time.time_ns()
    print(end - start)
