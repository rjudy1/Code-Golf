# Advent of Code 2022 Day 10
# Author:   Rachael Judy
# Date:     12/10/22
# Purpose:

import parseMod
import time
start = time.time()

stage = 'a'
day = 10
year = 2022
parseMod.createDataFile(year=year, day=day)
path = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ' ')


if stage == 'a':

else:


print("SUBMITTING RESULT: ", result)
print(f"Time: {time.time()-start}")
parseMod.submit(result, part=stage, day=day, year=year)
