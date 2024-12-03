# Advent of Code 2024 Day 4
# Author:   Rachael Judy
# Purpose:

import parseMod


ready = False
day = 4
stage = 'a'  #
year = 2024

parseMod.createDataFile(year=year, day=day)
memory = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")




if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
