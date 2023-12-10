# Advent of Code 2023 Day 10
# Author:   Rachael Judy
# Date:     12/10/23
# Purpose:  find main loop in a mess of pipes and find area enclosed by loop (expand and bfs, shoelace might be better, a little messy and slow)

import copy
import math
import parseMod

ready = True
day = 10
stage = 'b'
year = 2023

parseMod.createDataFile(year=year, day=day)
map = [list(row) for row in parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")]

for idx, row in enumerate(map):  # find starting position for loop
    if 'S' in row:
        start = idx, row.index('S')

directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
adjacencies = {'|': [(-1, 0), (1, 0)], '-': [(0, -1), (0, 1)], '7': [(1, 0), (0, -1)],
               'F': [(1, 0), (0, 1)], 'J': [(-1, 0), (0, -1)], 'L': [(-1, 0), (0, 1)]}
start_adj = list()
for dr, dc in directions:  # find out which direction the route goes
    for adj in adjacencies:
        if map[start[0] + dr][start[1] + dc] == adj and (dr == -adjacencies[adj][0][0] and dc == -adjacencies[adj][0][1]
                                                         or dr == -adjacencies[adj][1][0] and dc == -adjacencies[adj][1][1]):
            start_adj.append((start[0] + dr, start[1] + dc))

map_copy = copy.deepcopy(map)  # for annotation of actual route
map_copy[start[0]][start[1]] = 'M'  # M indicates part of main loop
position, past, step = start_adj[0], start, 1  # first step is in direction of adjacency next to start
while position != start:  # walk the loop
    for adj in adjacencies:
        if map[position[0]][position[1]] == adj:
            d0, d1 = adjacencies[adj]
            dr, dc = d1 if past == (position[0] + d0[0], position[1] + d0[1]) else d0
            map_copy[position[0]][position[1]] = 'M'  # M indicates part of main loop
            past, position = position, (position[0] + dr, position[1] + dc)
            step += 1
result = math.ceil(step / 2)

if stage == 'b':
    for adj in adjacencies:  # find out what type of pipe we have for s
        if (start[0] + adjacencies[adj][0][0], start[1] + adjacencies[adj][0][1]) == start_adj[0] and \
                (start[0] + adjacencies[adj][1][0], start[1] + adjacencies[adj][1][1]) == start_adj[1] or \
                (start[0] + adjacencies[adj][0][0], start[1] + adjacencies[adj][0][1]) == start_adj[1] and \
                (start[0] + adjacencies[adj][1][0], start[1] + adjacencies[adj][1][1]) == start_adj[0]:
            map[start[0]][start[1]] = adj

    for i, row in enumerate(map_copy):  # mark all non route spots as '.'
        for c, col in enumerate(row):
            map[i][c] = '.' if col != 'M' else map[i][c]

    map_copy = map.copy()  # copy map so it can be extended to open gaps
    for i in range(len(map) - 1, 0, -1):  # add row between every row
        new_row = ['|' if map[i][j] == '|' or map[i][j] == 'L' or map[i][j] == 'J' else '.' for j, col in enumerate(map[i])]
        map_copy.insert(i, new_row)
    for i, row in enumerate(map_copy):  # expand the columns in the copy
        new_row = row.copy()
        for j in range(len(row) - 1, 0, -1):
            if row[j] == '-' or row[j] == '7' or row[j] == 'J':
                new_row.insert(j, '-')
            else:
                new_row.insert(j, '.')
        map_copy[i] = new_row

    result = 0
    for i, row in enumerate(map_copy):
        for j, col in enumerate(row):
            if i % 2 == 0 and j % 2 == 0 and col == '.':
                # bfs to an edge
                visited = {(i, j)}
                queue = [(i, j)]
                edge = False
                while len(queue) and not edge:
                    x, y = queue.pop(0)
                    edge = (x == 0 or x == len(map_copy) - 1 or y == 0 or y == len(row) - 1)
                    for dx, dy in directions:
                        if (x + dx, y + dy) not in visited and 0 <= x + dx < len(map_copy)\
                                and 0 <= y + dy < len(row) and map_copy[x + dx][y + dy] == '.':
                            visited.add((x + dx, y + dy))
                            queue.append((x + dx, y + dy))
                result += int(not edge)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
