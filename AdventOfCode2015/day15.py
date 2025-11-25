# Advent of Code 2015 Day 15
# Author:   Rachael Judy
# Purpose:  mixed integer maximization of score s.t. calorie and ingredient limit (brute force combos)

import itertools
import numpy as np

import parseMod

ready = False
day = 15
stage = 'a'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl('data/' + str(day).zfill(2) + 'data.csv')

stats = np.array([[int(row[i].strip(',')) for i in range(2, 11, 2)] for row in data])
result = max(int(np.prod([max(0, np.dot(stats[:, r], [*x, 100-sum(x)])) for r in range(4)]))
             for x in itertools.combinations_with_replacement(range(101), len(data)-1)
             if stage != 'b' or np.dot(stats[:, 4], [*x, 100-sum(x)]) == 500)

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
