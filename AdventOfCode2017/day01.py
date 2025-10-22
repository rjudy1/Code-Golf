# Advent of Code 2017 Day 1
# Author:   Rachael Judy
# Purpose:  sum all values that immediately match the next digit/halfway digit


import parseMod

ready = False
day = 1
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = [int(i) for i in parseMod.readCSV_single("data/" + str(day).zfill(2) + "data.csv")]

result = sum(data[i] for i in range(len(data))
             if data[i] == data[i-1] and stage == 'a' or data[i] == data[i-len(data)//2] and stage == 'b')

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
