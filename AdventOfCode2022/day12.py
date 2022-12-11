# Advent of Code 2022 Day 12
# Author:   Rachael Judy
# Date:     12/12/22
# Purpose:

import math
import parseMod
import time

start = time.time()
stage = 'a'
day = 12
year = 2022
parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")


if stage == 'a':
    rounds, div, = 20, 3
else:
    rounds, div = 10000, 1

print("SUBMITTING RESULT: ", result)
print(f"Time: {time.time()-start}")
parseMod.submit(result, part=stage, day=day, year=year)
