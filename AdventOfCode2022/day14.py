# Advent of Code 2022 Day 14
# Author:   Rachael Judy
# Date:     12/14/22
# Purpose:

import parseMod
import time

start = time.time()
stage = 'a'
day = 14
year = 2022
parseMod.createDataFile(year=year, day=day)
line_list = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

print("SUBMITTING RESULT: ", result)
print(f"Time: {time.time()-start}")
parseMod.submit(result, part=stage, day=day, year=year)
