# Advent of Code 2015 Day 24
# Author:   Rachael Judy
# Purpose:  find min size, min prod of 3/4 equal weight groups

from itertools import combinations
from math import prod

import parseMod

ready = True
day = 24
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = set(reversed(parseMod.readCSVInts(f'data/{day:02d}data.csv')))

gs, w = 3 + (stage == 'b'), sum(data) // (3 + (stage == 'b'))
partition = lambda ns, gt: gt == 1 and sum(ns) == w or any(sum(g) == w and partition(ns-set(g), gt - 1) for k in range(2, len(ns)) for g in combinations(ns, k))
result = next(prod(g) for r in range(1, len(data)) for g in sorted((c for c in combinations(data, r) if sum(c) == w), key=prod) if partition(data - set(g), gs - 1))

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
