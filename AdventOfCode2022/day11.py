# Advent of Code 2022 Day 11
# Author:   Rachael Judy
# Date:     12/11/22
# Purpose:

import parseMod
import time
start = time.time()

stage = 'a'
day = 11
year = 2022
parseMod.createDataFile(year=year, day=day)
instructions = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ' ')


if stage == 'a':
    result = score
else:
    print("OUTPUT for B cannot be submitted as standard")


print("SUBMITTING RESULT: ", result)
print(f"Time: {time.time()-start}")
parseMod.submit(result, part=stage, day=day, year=year)
