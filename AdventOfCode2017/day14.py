# Advent of Code 2017 Day 14
# Author:   Rachael Judy
# Purpose:  use day 10b to execute knot hash and count 1s

from functools import reduce
import networkx as nx
from operator import xor

import parseMod

ready = True
day = 14
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")[0]
inputs = [data + f"-{i}" for i in range(128)]


def knot_hash(s: str) -> str:  # from day 10, could do in place for speed but i'm choosing compactness for now
    lengths = list(map(ord, s)) + [17, 31, 73, 47, 23]
    array = list(range(256))
    skip = current_pos = 0
    for _ in range(64):
        for length in lengths:  # perform hashing
            segment = [(current_pos + i) % len(array) for i in range(length)]  # could do in place instead
            for i, v in zip(segment, reversed([array[j] for j in segment])):
                array[i] = v
            current_pos = (current_pos + length + skip) % len(array)
            skip += 1

    return ''.join(f'{reduce(xor, array[i:i+16]):02x}' for i in range(0, 256, 16))


# could do these simultaneously in a loop instead to half the time
used = sum(bin(int(knot_hash(line), 16))[2:].count('1') for line in inputs)
grid = [bin(int(knot_hash(line), 16))[2:].zfill(128) for line in inputs]
graph = nx.Graph()
for i in range(128):
    for j in range(128):
        if grid[i][j] == '1':
            graph.add_node((i,j))
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                if 0 <= i+di < 128 and 0 <= j+dj < 128 and grid[i+di][j+dj] == grid[i][j]:
                    graph.add_edge((i,j), (i+di,j+dj))

result = used if stage=='a' else nx.number_connected_components(graph)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
