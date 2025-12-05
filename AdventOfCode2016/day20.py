# Advent of Code 2016 Day 20
# Author:   Rachael Judy
# Purpose:  find numbers < 2**32 that are not in the listed ranges

import parseMod

ready = True
day = 20
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = sorted([tuple(map(int, ns.split('-'))) for ns in parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')])

folded_ranges, lc, uc = 0, 0, -1
for l, u in data:
    if l > uc + 1:
        if stage == 'a': break
        folded_ranges += uc - lc + 1
        lc = l
    uc = max(u, uc)
result = uc+1 if stage == 'a' else (1 << 32) - (folded_ranges + uc - lc + 1)

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
