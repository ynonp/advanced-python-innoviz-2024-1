"""
https://adventofcode.com/2016/day/8
"""
import numpy as np
import re

class Screen:
    def __init__(self):
        self.screen = np.zeros((6, 50), dtype=bool)

    def rect(self, rows: int, columns: int):
        self.screen[0:rows, 0:columns] = True

    def rotate_column(self, column: int, by: int):
        self.screen[:, column] = np.roll(self.screen[:, column], by)

    def rotate_row(self, row: int, by: int):
        self.screen[row] = np.roll(self.screen[row], by)

    def __str__(self):
        return ('\n'
                .join(''
                      .join(np.where(
            self.screen, "#", ".")[i]) for i in range(len(self.screen))))

s = Screen()
# s.rect(rows=2, columns=3)
# s.rotate_column(column=1, by=1)
# s.rotate_row(0, 4)
# s.rotate_column(1, 1)
# print(s)

with open('input.txt', encoding='utf8') as in_file:
    for line in in_file:
        if m := re.search(r'rect (\d+)x(\d+)', line):
            columns, rows = m.groups()
            s.rect(rows=int(rows), columns=int(columns))

        elif m := re.search(r'rotate row y=(\d+) by (\d+)', line):
            row, by = m.groups()
            s.rotate_row(int(row), int(by))

        elif m := re.search(r'rotate column x=(\d+) by (\d+)', line):
            column, by = m.groups()
            s.rotate_column(int(column), int(by))

        else:
            print(f"Unrecognized line: {line}")
            pass


    print(s)











