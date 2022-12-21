# Advent of Code 2022 Day 22
# Author:   Rachael Judy
# Date:     12/22/22
# Purpose:

import parseMod
import time

stage = 'a'
day = 22
year = 2022
parseMod.createDataFile(year=year, day=day)
nums = parseMod.readCSV_rowEl(f"data/{str(day).zfill(2)}data.csv", ' ')
start = time.time()



if stage == 'a':
    result = monkeys['root']
else:
    result = monkeys['humn']

print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
