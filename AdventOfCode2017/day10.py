# Advent of Code 2017 Day 10
# Author:   Rachael Judy
# Purpose:  perform knot hash and convert output of extended hash to hex

from functools import reduce
from operator import xor

import parseMod

ready = True
day = 10
stage = 'a'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")[0]

lengths = list(map(ord, data)) + [17, 31, 73, 47, 23] if stage == 'b' else list(map(int, data.split(',')))
array = list(range(256))
skip = current_pos = 0
for _ in range(64 if stage == 'b' else stage == 'a'):
    for length in lengths:  # perform hashing
        segment = [(current_pos + i) % len(array) for i in range(length)]  # could do in place instead
        for i, v in zip(segment, reversed([array[j] for j in segment])):
            array[i] = v
        current_pos = (current_pos + length + skip) % len(array)
        skip += 1

result = array[0] * array[1] if stage == 'a' else ''.join(f'{reduce(xor, array[i:i+16]):02x}' for i in range(0, 256, 16))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
