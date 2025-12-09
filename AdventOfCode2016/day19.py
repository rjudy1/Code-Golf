# Advent of Code 2016 Day 19
# Author:   Rachael Judy
# Purpose:  josephus problem k=2 and k=3

import math

import parseMod

ready = True
day = 19
stage = 'a'
year = 2016

parseMod.createDataFile(year=year, day=day)
N = parseMod.readCSVInts('data/' + str(day).zfill(2) + 'data.csv')[0]

result = 2 * (N - (1 << (N.bit_length() - 1))) + 1 if stage == 'a' \
    else N if N == (p := 3 ** math.floor(math.log(N, 3))) else N-p if N <= 2*p else p + 2 * (N - 2 * p)

print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
