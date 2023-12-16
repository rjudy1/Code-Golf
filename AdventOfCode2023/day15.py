# Advent of Code 2023 Day 15
# Author:   Rachael Judy
# Date:     12/15/23
# Purpose:  hashing operation applied to assign labels and values into boxes

import collections
import functools
import parseMod

ready = True
day = 15
stage = 'b'
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")[0].split(',')

hashop = lambda line: functools.reduce(lambda prev, letter: 17*(prev+ord(letter)) % 256, [0, *list(line)])
result = sum(hashop(line) for line in data)  # stage a

if stage == 'b':
    box_map, label_map = collections.defaultdict(lambda: list()), dict()
    for datapoint in data:
        op0, op1 = datapoint.split('=' if '=' in datapoint else '-')
        box = hashop(op0)
        if '=' in datapoint:
            if op0 not in box_map[box]:
                box_map[box].append(op0)
            label_map[op0] = int(op1)
        elif '-' in datapoint and op0 in box_map[box]:
            box_map[box].remove(op0)

    result = sum(sum((i+1) * (j+1) * label_map[label] for j, label in enumerate(box_map[i])) for i in box_map)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
