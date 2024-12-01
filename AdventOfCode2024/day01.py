# Advent of Code 2023 Day 1
# Author:   Rachael Judy
# Date:     12/1/24
# Purpose:

import parseMod

ready = True
day = 1
stage = 'a'
year = 2024

# parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

nums = []

import collections
s1, s2 = list(), list()
d1, d2 = collections.defaultdict(lambda: list()), collections.defaultdict(lambda: list())
for i, line in enumerate(array):
    n1, n2 = line.split()
    s1.append(int(n1))
    s2.append(int(n2))
    d1[int(n1)].append(i)
    d2[int(n2)].append(i)

s1.sort()
s2.sort()
total_dist = 0
for n1, n2 in zip(s1, s2):
    total_dist += abs(d1[n1].pop(0) - d2[n2].pop(0))
result = total_dist

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
