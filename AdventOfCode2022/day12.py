# Advent of Code 2022 Day 12
# Author:   Rachael Judy
# Date:     12/12/22
# Purpose:  djikstra maze

import parseMod
import time

start = time.time()
stage = 'b'
day = 12
year = 2022
parseMod.createDataFile(year=year, day=day)
elevations = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")
cost = [[10000 for _ in range(len(elevations[0]))] for _ in range(len(elevations))]

# find start and end
for i in range(len(elevations)):
    elevations[i] = [*elevations[i]]
    for j in range(len(elevations[0])):
        if elevations[i][j] == 'S':
            start_node = (i, j)
            cost[i][j] = 0
            elevations[i][j] = 'a'
        if elevations[i][j] == 'E':
            end_node = (i, j)
            elevations[i][j] = 'z'

directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
to_explore = [start_node]
while len(to_explore):
    n = to_explore.pop(0)
    for dir in directions:
        if 0 <= n[0] + dir[0] < len(elevations) \
                and 0 <= n[1] + dir[1] < len(elevations[0]) \
                and ord(elevations[n[0] + dir[0]][n[1] + dir[1]]) <= ord(elevations[n[0]][n[1]]) + 1 \
                and cost[n[0] + dir[0]][n[1] + dir[1]] > cost[n[0]][n[1]] + 1:
            cost[n[0] + dir[0]][n[1] + dir[1]] = (cost[n[0]][n[1]] + 1) \
                if elevations[n[0] + dir[0]][n[1] + dir[1]] != 'a' or stage == 'a' else 0
            to_explore.append((n[0] + dir[0], n[1] + dir[1]))

result = cost[end_node[0]][end_node[1]]

print("SUBMITTING RESULT: ", result)
print(f"Time: {time.time() - start}")
parseMod.submit(result, part=stage, day=day, year=year)
