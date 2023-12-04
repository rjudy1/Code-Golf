# Advent of Code 2023 Day 5
# Author:   Rachael Judy
# Date:     12/5/23
# Purpose:

from collections import defaultdict

import parseMod

ready = True
day = 5
stage = 'a'

year = 2023

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")



if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
