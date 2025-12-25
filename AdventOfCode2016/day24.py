# Advent of Code 2016 Day 24
# Author:   Rachael Judy
# Purpose:  hamiltonian path and circuit

from itertools import permutations
from functools import cache
import networkx as nx

import parseMod

ready = True
day = 24
stage = 'b'
year = 2016

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row('data/' + str(day).zfill(2) + 'data.csv')

G = nx.Graph([(i+j*1j, i+j*1j+dx) for i, row in enumerate(data) for j, col in enumerate(row) for dx in {1, -1, -1j, 1j} 
              if col != '#' and 0 <= (k := i+j*1j+dx).real < len(data) and 0 <= k.imag < len(data[0]) and data[int(k.real)][int(k.imag)] != '#'])
targets = {i+1j*j for i, row in enumerate(data) for j, col in enumerate(row) if col.isdigit() and col != '0'}
start = [i+1j*j for i, row in enumerate(data) for j, col in enumerate(row) if col == '0'][0]

@cache
def shortest_path(a, b):
    return nx.shortest_path_length(G, a, b)

result = min(sum(shortest_path(path[i], path[i+1]) for i in range(len(path)-1)) for order in permutations(targets)
             if (path := [start] + list(order) + ([] if stage == 'a' else [start])))
print(f'result: \n{result}')
if ready:
    parseMod.submit(result, part=stage, day=day, year=year)
