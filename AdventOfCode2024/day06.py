# Advent of Code 2024 Day 6
# Author:   Rachael Judy
# Purpose:

import collections
import numpy as np
import parseMod

ready = True
day = 6
stage = 'a'
year = 2024

parseMod.createDataFile(year=year, day=day)
rules, instructions = parseMod.readCSV_chunk("data/" + str(day).zfill(2) + "data.csv")



if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
