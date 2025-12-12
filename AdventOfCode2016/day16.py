# Advent of Code 2016 Day 16
# Author:   Rachael Judy
# Purpose:  bit-twiddling expansions and compaction

import numpy as np

import parseMod

ready = True
day = 16
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')[0]

def expand_and_checksum(size, a_str):
    a = np.frombuffer(a_str.encode(), dtype=np.uint8) - 48
    while a.size < size:  # expansion
        a = np.concatenate((a, np.array([0], np.uint8), 1 - a[::-1]))  # reverse and invert bits
    a = a[:size]  # trim to required size
    while a.size % 2 == 0:  # checksum
        a = (a[0::2] == a[1::2]).astype(np.uint8)  # pairwise compare → bit
    return "".join(a.astype(str))

result = expand_and_checksum(35651584 if stage == 'b' else 272, (data))
print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
