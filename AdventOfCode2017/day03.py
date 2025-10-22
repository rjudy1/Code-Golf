# Advent of Code 2023 Day 1
# Author:   Rachael Judy
# Purpose:  sum all values that immediately match the next digit

import numpy as np

import parseMod

ready = True
day = 3
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSVInts("data/" + str(day).zfill(2) + "data.csv")[0]
print(data)




if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
