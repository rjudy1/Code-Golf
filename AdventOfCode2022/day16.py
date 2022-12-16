# Advent of Code 2022 Day 16
# Author:   Rachael Judy
# Date:     12/16/22
# Purpose:

import parseMod
import time

stage = 'a'
day = 16
year = 2022
# parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")
start = time.time()



print(f"Time: {time.time() - start}")
print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
