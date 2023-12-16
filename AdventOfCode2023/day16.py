# Advent of Code 2023 Day 16
# Author:   Rachael Judy
# Date:     12/16/23
# Purpose:  Fire beams of light through mirrors, store number of spaces beam passes through

import parseMod

ready = True
day = 16
stage = 'b'
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

result = 0
directions = lambda r, c: {'|': {(c, 0), (-c, 0)}, '-': {(0, c)}, '.': {(0, c)}, '\\': {(c, 0)}, '/': {(-c, 0)}} \
    if r == 0 else {'|': {(r, 0)}, '-': {(0, r), (0, -r)}, '.': {(r, 0)}, '\\': {(0, r)}, '/': {(0, -r)}}
ranges = [(0, 0, 0, 0, 0, 1)] if stage == 'a' else \
    [(0, 0, 0, len(data[0]) - 1, 1, 0), (len(data) - 1, len(data) - 1, 0, len(data[0]) - 1, -1, 0),
     (0, len(data) - 1, 0, 0, 0, 1), (0, len(data) - 1, len(data[0]) - 1, len(data[0]) - 1, 0, -1)]

for row0, row1, col0, col1, d0, d1 in ranges:
    for i in range(row0, row1 + 1):
        for j in range(col0, col1 + 1):
            queue = [(i, j, *d) for d in directions(d0, d1)[data[i][j]]]  # position, direction
            visited = {(i, j, *d) for d in directions(d0, d1)[data[i][j]]}
            while len(queue):  # bfs
                row, col, dr, dc = queue.pop(0)
                if 0 <= row + dr < len(data) and 0 <= col + dc < len(data[0]):
                    for d in directions(dr, dc)[data[row + dr][col + dc]]:
                        if (row + dr, col + dc, *d) not in visited:
                            queue.append((row + dr, col + dc, *d))
                            visited.add((row + dr, col + dc, *d))
            result = max(result, len(set((v[0], v[1]) for v in visited)))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
