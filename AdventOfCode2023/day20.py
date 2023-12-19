# Advent of Code 2023 Day 20
# Author:   Rachael Judy
# Date:     12/20/23
# Purpose:

import parseMod

ready = True
day = 20
stage = 'a'
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_chunk("data/" + str(day).zfill(2) + "data.csv")



if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
