# with open('/etc/passwd') as f:
#     for line in f: print(line)

import sys
file_handle = open('/etc/passwd')
try:
    f = file_handle.__enter__()
    try:
        while True:
            line = f.__next__()
            print(line.__str__())
    except StopIteration:
        pass
finally:
    file_handle.__exit__(...)



