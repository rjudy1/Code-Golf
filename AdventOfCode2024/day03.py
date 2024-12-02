# Advent of Code 2024 Day 3
# Author:   Rachael Judy
# Purpose:

import parseMod
import copy

ready = False
day = 3
stage = 'a'
year = 2024

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")



if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
