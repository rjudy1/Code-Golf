# Advent of Code 2024 Day 12
# Author:   Rachael Judy
# Purpose:  find area (bfs) and perimeter/number of sides (corners) of regions in a grid

import collections
import csv
import parseMod

ready = True
day = 12
stage = 'a'  # 1522850, 953738
year = 2024

parseMod.createDataFile(year=year, day=day)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    garden = collections.defaultdict(str)
    for i, row in enumerate(reader):
        for j, col in enumerate(row[0]):
            garden[complex(i,j)] = col

result = 0
visited = set()
dirs = [1, 1j, -1, -1j]
for plot in list(garden.keys()):
    if plot in visited:
        continue

    queue = collections.deque([plot])
    perimeter, sides, size_visited_prior = 0, 0, len(visited)
    visited.add(plot)
    while queue:
        node = queue.popleft()
        for dx in dirs:
            perimeter += 1 if garden[node + dx] != garden[plot] else 0  # if outer edge
            if garden[node + dx] == garden[plot] and node + dx not in visited:
                visited.add(node + dx)
                queue.append(node + dx)
        for i in range(len(dirs)):  # check all perpendicular direction pairs to detect inner/outer corner
            if (garden[node + dirs[i]] != garden[plot] and garden[node + dirs[(i + 1) % 4]] != garden[plot] or
                    garden[node + dirs[i]] == garden[node + dirs[(i + 1) % 4]] and garden[node + dirs[i] + dirs[(i + 1) % 4]] != garden[plot]):
                sides += 1
    result += (perimeter if stage == 'a' else sides)*(len(visited) - size_visited_prior)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
