# Advent of Code 2022 Day 3
# Author:   Rachael Judy
# Date:     12/3/22
# Purpose:

import parseMod

ready = False
day = 3
stage = 'a'

year = 2022

parseMod.createDataFile(year=year, day=day)
guide = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ' ')

# ord('W') == 87, ord('@') == 64
if stage == 'a':
    pass
else:
    pass

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
