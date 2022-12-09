# Advent of Code 2022 Day 9
# Author:   Rachael Judy
# Date:     12/9/22
# Purpose:  snake but tries to keep in the same col or row instead of simple following head

import math
import parseMod
import time
start = time.time()

stage = 'b'
day = 9
year = 2022
parseMod.createDataFile(year=year, day=day)
path = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", ' ')


def move_knot(tail, new_head):
    if math.sqrt(pow(new_head[0] - tail[0], 2) + pow(new_head[1] - tail[1], 2)) >= 2:
        dxdy = ((new_head[0] - tail[0]) / 2, (new_head[1] - tail[1]) / 2)
        tail = (tail[0] + (math.ceil(dxdy[0]) if dxdy[0] > 0 else math.floor(dxdy[0])),
                tail[1] + (math.ceil(dxdy[1]) if dxdy[1] > 0 else math.floor(dxdy[1])))
    return tail


def solve(moves, knot_count):
    direction_map = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}
    visited = {(0, 0)}
    positions = [(0, 0) for _ in range(knot_count)]
    for dire, step in moves:
        for _ in range(int(step)):
            positions[0] = (positions[0][0] + direction_map[dire][0], positions[0][1] + direction_map[dire][1])
            for i in range(1, knot_count):
                former_position = positions[i]
                positions[i] = move_knot(positions[i], positions[i-1])
                if positions[i] == former_position: break
            visited.add(positions[-1])

    return len(visited)


if stage == 'a':
    result = solve(path, 2)
else:
    result = solve(path, 10)

print("SUBMITTING RESULT: ", result)
print(f"Time: {time.time()-start}")
parseMod.submit(result, part=stage, day=day, year=year)
