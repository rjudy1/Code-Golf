# Advent of Code 2015 Day 13
# Author:   Rachael Judy
# Purpose:  score happiest permutation of seating input + self

from collections import defaultdict
from itertools import permutations

import parseMod

ready = False
day = 13
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl('data/' + str(day).zfill(2) + 'data.csv')

hw = defaultdict(int, {(r[0], r[-1].strip('.')): -int(r[3]) if r[2] == 'lose' else int(r[3]) for r in data})
pp = {r[0] for r in data}
if stage == 'b':
    pp.add("R")
result = max(sum(hw[ar[i], ar[(i+1)%len(pp)]] + hw[ar[(i+1)%len(pp)], ar[i]] for i in range(len(ar))) for ar in permutations(pp))

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
