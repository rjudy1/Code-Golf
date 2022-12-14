# Advent of Code 2022 Day 15
# Author:   Rachael Judy
# Date:     12/15/22
# Purpose:

import parseMod
import time

start = time.time()
stage = 'a'
day = 15
year = 2022
parseMod.createDataFile(year=year, day=day)
rocks = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")



print("SUBMITTING RESULT: ", result)
print(f"Time: {time.time() - start}")
parseMod.submit(result, part=stage, day=day, year=year)
