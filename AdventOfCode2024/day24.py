# Advent of Code 2024 Day 24
# Author:   Rachael Judy
# Purpose:

import csv
import parseMod

ready = True
day = 24
stage = 'a'  #
year = 2024

parseMod.createDataFile(year=year, day=day)

with open("data/" + str(day).zfill(2) + "data.csv") as file:
    for i, row in enumerate(csv.reader(file)):
        pass


if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
