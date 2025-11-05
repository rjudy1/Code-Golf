# Advent of Code 2017 Day 11
# Author:   Rachael Judy
# Purpose:  hex coordinates (3D, sort of)

from dataclasses import dataclass

import parseMod

ready = True
day = 11
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ',')[0]

dirs = {'n': (0, 1, -1), 'ne': (1, 0, -1), 'se': (1, -1, 0),
        's': (0, -1, 1), 'sw': (-1, 0, 1), 'nw': (-1, 1, 0)}
pos, max_dist = (0, 0, 0), 0
for d in data:
    pos = tuple(x + y for x, y in zip(pos, dirs[d]))
    max_dist = max(max_dist, max(abs(x) for x in pos))
result = max(abs(x) for x in pos) if stage == 'a' else max_dist

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
