# Advent of Code 2024 Day 7
# Author:   Rachael Judy
# Purpose:  find combination of operators (+,*,||) that make equations work with BFT search (take that, exponential)

import collections
import csv
import math

import parseMod

ready = True
day = 7
stage = 'b'
year = 2024

parseMod.createDataFile(year=year, day=day)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    equations = [row[0] for row in reader]

result = 0
for row in equations:
    cache = dict()
    a, opers = int(row.split(':')[0]), [int(o) for o in row.split(':')[1].split()]

    # BFT this, starting from the top node
    queue = collections.deque([(a,len(opers)-1)])
    while queue:
        v, ind = queue.popleft()
        if v == opers[0] and ind == 0:
            result += a
            break
        if v % opers[ind] == 0 and ind > 0:
            queue.append((v // opers[ind], ind - 1))
        if v - opers[ind] > 0 and ind > 0:
            queue.append((v - opers[ind], ind - 1))
        if stage == 'b' and ind > 0 and v % 10**(math.ceil(math.log10(opers[ind] + 1))) == opers[ind] and v > opers[ind]:
            queue.append(((v - opers[ind]) // (10 ** (math.ceil(math.log10(opers[ind] + 1)))), ind - 1))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
