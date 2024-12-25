# Advent of Code 2024 Day 18
# Author:   Rachael Judy
# Purpose:
# so slow with the repeated search, clean this up with dfs

import collections
import csv
import math
import parseMod

ready = True
day = 18
stage = 'a'
year = 2024

parseMod.createDataFile(year=year, day=day)
costs = collections.defaultdict(lambda: math.inf)
map = collections.defaultdict(str)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        for j, col in enumerate(row[0]):
            map[complex(i,j)] = col
            if col == 'S':
                queue = collections.deque([(complex(i,j), 1j)])
                costs[(complex(i,j), 1j)] = 0



if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
