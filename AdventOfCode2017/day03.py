# Advent of Code 2017 Day 3
# Author:   Rachael Judy
# Purpose:  use incrementing spiral and sum of existing neighbors spiral to find distance to value and value > input

from collections import defaultdict

import parseMod

ready = True
day = 3
stage = 'a'
year = 2017

import math

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSVInts("data/" + str(day).zfill(2) + "data.csv")[0]
print(data)

# no code needed for today but we'll write some for reference
# note sequence of odd squares from bottom right corner and just walk around the perimeter
# find nearest higher odd
lower_right_root = math.ceil(math.sqrt(data)) + int(math.ceil(math.sqrt(data)) % 2 == 0)
# figure out which side of the square the value is in and then distance from the nearest center
# lower left is lower_right^2 - lower right_root +1
print(lower_right_root)

# for b, just build with existing, moving in spiral pattern
visited = defaultdict(int)
visited[(0, 0)] = 1
# move in spiral pattern with break off too right, sum neighbors
sum(visited[x+dx,y+dy] for (dx, dy) in [(-1,-1), (-1, 0), (-1, 1), (0,-1), (0,1), (1, -1), (1,0), (1,1)])

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
