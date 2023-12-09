# Advent of Code 2023 Day 8
# Author:   Rachael Judy
# Date:     12/8/23
# Purpose:  count steps in following graph to ZZZ and then from all ending in A to something simultaneously ending in Z
# This is not a general solution for any input graph with the given rules, input is curated for LCM instead of CRT

import math
import parseMod

ready = True
day = 8
stage = 'a'
year = 2023

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", delim='=')

graph = dict()
for source, dests in array[2:]:
    graph[source.strip()] = [a.strip() for a in dests[2:-1].split(',')]

lr_to_dir = lambda dir: 0 if dir == 'L' else 1
steps = 0
if stage == 'a':
    position = 'AAA'
    while position != 'ZZZ':
        position = graph[position][lr_to_dir(array[0][0][steps % len(array[0][0])])]
        steps += 1
    result = steps
else:
    positions = list(filter(lambda a: a[2] == 'A', graph))  # positions ending with A
    found_z = [-1 for i in range(len(positions))]  # first location on this node that ends with Z
    while found_z.count(-1) != 0:
        for i, p in enumerate(positions):
            positions[i] = graph[p][lr_to_dir(array[0][0][steps % len(array[0][0])])]
            if positions[i][2] == 'Z' and found_z[i] == -1:
                found_z[i] = steps + 1
        steps += 1
    result = math.lcm(*found_z)  # lcm of first occurrence of z end, pattern noted for all caught in loop

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
