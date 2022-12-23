# Advent of Code 2022 Day 24
# Author:   Rachael Judy
# Date:     12/24/22
# Purpose:  keep spreading out elves until sufficiently spaced given scatter rules

import parseMod
import time

stage = 'a'
day = 24
year = 2022
parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row(f"data/{str(day).zfill(2)}data.csv")
start = time.time()



if stage == 'a':
    result = (max_y - min_y + 1) * (max_x - min_x + 1) - len(elves)
else:
    result = move(elves, 10000) + 1

print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
