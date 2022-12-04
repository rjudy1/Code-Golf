# Advent of Code 2022 Day 5
# Author:   Rachael Judy
# Date:     12/5/22
# Purpose:

import parseMod

ready = False
day = 5
stage = 'a'

year = 2022

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ',')


if stage == 'a':
    pass
else:
    pass

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
