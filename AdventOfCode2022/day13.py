# Advent of Code 2022 Day 13
# Author:   Rachael Judy
# Date:     12/13/22
# Purpose:

import parseMod
import time

start = time.time()
stage = 'a'
day = 13
year = 2022
parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")


result = cost[end_node[0]][end_node[1]]

print("SUBMITTING RESULT: ", result)
print(f"Time: {time.time()-start}")
parseMod.submit(result, part=stage, day=day, year=year)
