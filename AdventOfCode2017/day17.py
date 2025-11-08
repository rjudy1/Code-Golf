# Advent of Code 2017 Day 17
# Author:   Rachael Judy
# Purpose:  circular buffer (linked list) adding after input steps and tracking after 2017 and 0

from collections import deque

import parseMod

ready = True
day = 17
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSVInts("data/" + str(day).zfill(2) + "data.csv", ',')[0]

if stage == 'a':
    spinlock = deque([0])
    for i in range(1, 2017 + 1):
        spinlock.rotate(-data)
        spinlock.append(i)
    result = spinlock[(spinlock.index(2017) + 1) % len(spinlock)]
else:  # the key to stage b is you have to only track who is after zero which never moves
    index, result = 0, 0
    for i in range(1, 5000000 + 1):
        index = ((index + data) % i + 1) % (i + 1)
        if index == 1:  # placed right after zero
            result = i

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
