# Advent of Code 2017 Day 5
# Author:   Rachael Judy
# Purpose:  instruction jump counter with incrementing instructions

import parseMod

ready = True
day = 5
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSVInts("data/" + str(day).zfill(2) + "data.csv")

counter, result = 0, 0
while 0 <= counter < len(data):
    data[counter], counter = (data[counter] - 1, counter + data[counter]) if data[counter] >= 3 and stage == 'b' \
        else (data[counter] + 1, counter + data[counter])
    result += 1

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
