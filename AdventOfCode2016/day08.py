# Advent of Code 2016 Day 8
# Author:   Rachael Judy
# Purpose:  circular shift rows/columns (only a can be auto submitted, b must be visually inspected)

import numpy as np

import parseMod

ready = False
day = 8
stage = 'a'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl('data/' + str(day).zfill(2) + 'data.csv')

screen = np.zeros((6, 50), dtype=int)
for cmd, *args in data:
    if cmd == "rect":
        A, B = map(int, args[0].split("x"))
        screen[:B, :A] = 1
    elif cmd == "rotate":
        xy, n = int(args[1].split("=")[1]), int(args[3])
        if args[0] == "row":
            screen[xy] = np.roll(screen[xy], n)
        else:
            screen[:, xy] = np.roll(screen[:, xy], n)

print(f'result: \n{(result := np.count_nonzero(screen))}')
print("display:\n", "\n".join("".join("@" if c else "." for c in row) for row in screen), sep='')  # b) EOARGPHYAO
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
