# Advent of Code 2023 Day 10
# Author:   Rachael Judy
# Date:     12/10/23
# Purpose:


import parseMod

ready = True
day = 9
stage = 'a'
year = 2023

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv")


if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
