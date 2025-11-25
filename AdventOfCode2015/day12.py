# Advent of Code 2015 Day 12
# Author:   Rachael Judy
# Purpose:  process flattened json to sum numbers and numbers not in a red object

import json

import parseMod

ready = True
day = 12
stage = 'b'
year = 2015

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')[0]

def sum_without_red(data, ignore_red):
    if isinstance(data, dict):
        if "red" in data.values() and ignore_red:
            return 0
        return sum(sum_without_red(v, ignore_red) for v in data.values())
    elif isinstance(data, list):
        return sum(sum_without_red(v, ignore_red) for v in data)
    elif isinstance(data, int):
        return data
    return 0
result = sum_without_red(json.loads(data), stage=='b')

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
