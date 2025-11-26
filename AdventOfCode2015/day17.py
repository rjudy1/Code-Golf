# Advent of Code 2015 Day 17
# Author:   Rachael Judy
# Purpose:  count combos/min count combos of containers storing 150 units

from itertools import combinations

import parseMod

ready = False
day = 17
stage = 'a'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSVInts('data/' + str(day).zfill(2) + 'data.csv')

result = 0
for i in range(len(data)+1):
    result += sum(1 for c in combinations(range(len(data)), i) if sum(data[j] for j in c) == 150)
    if stage == 'b' and result:
        break

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
