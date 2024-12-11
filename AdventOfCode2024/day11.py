# Advent of Code 2024 Day 11
# Author:   Rachael Judy
# Purpose:  track counts for each stone type which changes according to rules over the number of blinks,
#               started with considering a patten as the blinks iterated, looked for repeated patterns in the 25 blink
#               chunks, realized no ordering needed, started chunks of 25 blinks and resultant counts with caching,
#               wandered off for a bit, realized count of each type can be maintained per blink and chunking was only
#               complicating what needed to be cached

import collections
import copy
import csv
import math

import parseMod

ready = True
day = 11
stage = 'b'  # 218079, 259755538429618
year = 2024

parseMod.createDataFile(year=year, day=day)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    stone_counts = collections.Counter([[int(r) for r in row[0].split()] for row in reader][0])


def blink(stone):  # could cache results, but already O(1)
    new_stones = list()
    if stone == 0:
        new_stones.append(1)
    elif math.ceil(math.log10(stone + 1)) % 2 == 0:
        new_stones.append(stone // 10 ** (math.ceil(math.log10(stone + 1)) // 2))
        new_stones.append(stone % 10 ** (math.ceil(math.log10(stone + 1)) // 2))
    else:
        new_stones.append(stone * 2024)
    return new_stones


for blinks in range(25 if stage == 'a' else 75):
    new_stone_counts = collections.defaultdict(int)
    for stone in stone_counts:
        produced = collections.Counter(blink(stone))
        for s in produced:
            new_stone_counts[s] += stone_counts[stone] * produced[s]  # number of source * number produced of s
    stone_counts = copy.deepcopy(new_stone_counts)
result = sum(stone_counts[s] for s in stone_counts)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
