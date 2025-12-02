# Advent of Code 2015 Day 25
# Author:   Rachael Judy
# Purpose:  diagonal population based only on previous value

import parseMod

ready = True
day = 25
stage = 'a'
year = 2015

parseMod.createDataFile(year=year, day=day)
r, c = tuple(int(x.strip(",.")) for x in parseMod.readCSV_rowEl(f"data/{day:02d}data.csv", " ")[0][-3::2])
result = 20151125 * pow(252533, (r + c - 2) * (r + c - 1) // 2 + c - 1, 33554393) % 33554393  # 19980801

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
