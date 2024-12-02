# Advent of Code 2023 Day 1
# Author:   Rachael Judy
# Date:     12/1/24
# Purpose:  Find mse difference between sorted values and then sum(value * freq2)

import collections

import parseMod

ready = False
day = 1
stage = 'a'
year = 2024

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

s1, s2 = sorted([int(n.split()[0]) for n in array]), sorted([int(n.split()[1]) for n in array])
f2 = collections.Counter(s2)
result = sum(abs(n1-n2) for n1, n2 in zip(s1, s2)) if stage == 'a' else sum(n1*f2[n1] for n1 in s1)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
