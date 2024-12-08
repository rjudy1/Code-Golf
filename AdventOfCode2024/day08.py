# Advent of Code 2024 Day
# Author:   Rachael Judy
# Purpose:  find nodes in line with antennas (equidistant and then all including antennas)

import collections
import csv
import itertools

import parseMod

ready = True
day = 8
stage = 'a'
year = 2024

parseMod.createDataFile(year=year, day=day)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    map = [row[0] for row in reader]

antinodes = set()
antenna_locations = collections.defaultdict(lambda: set())
for i, row in enumerate(map):
    for j, col in enumerate(row):
        if col != '.':
            antenna_locations[col].add(complex(i,j))
for ant in antenna_locations:  # for every antenna type
    for a1,a2 in itertools.combinations(antenna_locations[ant], 2):  # for every pair of antennas
        if a1 == a2:
            continue
        nodeA = a1-(a2-a1)
        if 0 <= nodeA.real < len(map) and 0 <= nodeA.imag < len(map[0]):
            antinodes.add(nodeA)
        nodeB = a2+(a2-a1)
        if 0 <= nodeB.real < len(map) and 0 <= nodeB.imag < len(map[0]):
            antinodes.add(nodeB)
        while stage == 'b' and 0 <= nodeA.real < len(map) and 0 <= nodeA.imag < len(map[0]):
            antinodes.add(nodeA)
            nodeA -= (a2-a1)
        nodeA = a1
        while stage == 'b' and 0 <= nodeA.real < len(map) and 0 <= nodeA.imag < len(map[0]):
            antinodes.add(nodeA)
            nodeA += (a2-a1)
result = len(antinodes)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
