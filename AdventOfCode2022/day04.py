# Advent of Code 2022 Day 4
# Author:   Rachael Judy
# Date:     12/4/22
# Purpose:  Subset and intersection checks
# - note that set is more concise but less efficient probably than brute force compares

import parseMod

ready = True
day = 4
stage = 'a'

year = 2022

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ',')

pairs = [[set(range(int(e.split('-')[0]), int(e.split('-')[1]) + 1)) for e in row] for row in data]

if stage == 'a':
    result = sum(1 if p[0].issubset(p[1]) or p[1].issubset(p[0]) else 0 for p in pairs)
else:
    result = sum(1 if len(p[0].intersection(p[1])) else 0 for p in pairs)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
