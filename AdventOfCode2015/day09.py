# Advent of Code 2015 Day 9
# Author:   Rachael Judy
# Purpose:  brute force a hamiltonian tour because why not

from itertools import permutations

import parseMod

ready = False
day = 9
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl(f'data/{day:02d}data.csv', ' ')

wt, cs = {pair: int(w) for a, _, b, _, w in data for pair in [(a, b), (b, a)]}, {x for d in data for x in (d[0], d[2])}
result = (min if stage == 'a' else max)(sum(wt[p[i], p[i+1]] for i in range(len(p)-1)) for p in permutations(cs))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print('SUBMITTING RESULT: ', result)
    parseMod.submit(result, part=stage, day=day, year=year)
