# Advent of Code 2022 Day 1
# Author:   Rachael Judy
# Date:     12/1/22
# Purpose:

import aocd
import parseMod

ready = False
day = 1
stage = 'a'

year = 2022

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV("data/" + str(day).zfill(2) + "data.csv", '\n')



result=array[0]

if not ready:
    print(result)
elif ready:
    print("SUBMITTING RESULT: ", result)
    print(aocd.submit(result, part="a", day=day, year=year))
