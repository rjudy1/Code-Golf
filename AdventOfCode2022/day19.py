# Advent of Code 2022 Day 19
# Author:   Rachael Judy
# Date:     12/19/22
# Purpose:

import parseMod
import time

stage = 'a'
day = 19
year = 2022
parseMod.createDataFile(year=year, day=day)
points = parseMod.readCSV_rowEl(f"data/{str(day).zfill(2)}data.csv", ',')
start = time.time()



if stage == 'a':
    result = count
else:
    result = count

print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
# parseMod.submit(result, part=stage, day=day, year=year)
