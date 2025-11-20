# Advent of Code 2015 Day 2
# Author:   Rachael Judy
# Purpose:  surface area + min surface slack, min perimeter + volume

import parseMod

ready = True
day = 2
stage = 'a'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

result = sum(2*(x*y + x*z + y*z) + min(x*y, y*z, x*z) if stage == 'a' else 2*min(x+y, y+z, x+z) + x*y*z
             for x, y, z in (map(int, line.split('x')) for line in data))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
