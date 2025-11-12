# Advent of Code 2017 Day 21
# Author:   Rachael Judy
# Purpose:

import parseMod

ready = True
day = 21
stage = 'a'
year = 2017

data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv", )




if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
