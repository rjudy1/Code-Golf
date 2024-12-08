# Advent of Code 2024 Day
# Author:   Rachael Judy
# Purpose:

import csv

import parseMod

ready = True
day = 9
stage = 'a'
year = 2024

parseMod.createDataFile(year=year, day=day)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    map = [row[0] for row in reader]



if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
