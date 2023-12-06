# Advent of Code 2023 Day 7
# Author:   Rachael Judy
# Date:     12/7/23
# Purpose:

import parseMod

ready = True
day = 7
stage = 'a'

year = 2023

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")



if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
