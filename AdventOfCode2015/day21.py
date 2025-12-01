# Advent of Code 2015 Day 21
# Author:   Rachael Judy
# Purpose:  boss battle min win, max loss based on hitpoints, defense

from itertools import combinations
import math

import parseMod

ready = False
day = 21
stage = 'a'
year = 2015

parseMod.createDataFile(year=year, day=day)
bh, bd, ba = (int(x[-1]) for x in parseMod.readCSV_rowEl(f'data/{day:02d}data.csv', ' '))
result = (min if stage == 'a' else max)(
    wc+ac+rc0+rc1
    for wc,wd,_ in [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)]
    for ac,_,aa in [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5), (0, 0, 0)]
    for (rc0,rd0,ra0),(rc1,rd1,ra1) in combinations([(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3), (0, 0, 0), (0, 0, 0)],2)
    if (math.ceil(bh / max(1, wd+rd0+rd1-ba)) <= math.ceil(100 / max(1, bd-aa-ra0-ra1)) if stage == 'a' else math.ceil(bh / max(1, wd+rd0+rd1-ba)) > math.ceil(100 / max(1, bd-aa-ra0-ra1))))

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
