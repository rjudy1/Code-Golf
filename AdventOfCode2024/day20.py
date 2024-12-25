# Advent of Code 2024 Day 20
# Author:   Rachael Judy
# Purpose:  count start-end defined cheats through walls for 1 or <20 steps that lead to saving 100+ steps

import collections
import csv
import parseMod

ready = True
day = 20
stage = 'b'  # 1307, 986545
year = 2024

parseMod.createDataFile(year=year, day=day)
grid = collections.defaultdict(str)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        for j, col in enumerate(row[0]):
            grid[complex(i, j)] = col
            if col == 'S':
                start = complex(i, j)
                grid[complex(i, j)] = '.'
            elif col == 'E':
                end = complex(i, j)
                grid[complex(i, j)] = '.'


def bfs(track, start):
    queue = collections.deque([(start, 0)])
    visited, distances = {start}, {start: 0}
    while queue:
        pos, dist = queue.popleft()
        distances[pos] = dist
        for dir in [1, -1, 1j, -1j]:
            if pos+dir not in visited and track[pos+dir] == '.':
                queue.append((pos+dir, dist+1))
                visited.add(pos+dir)
    return distances


result = 0
start_distances = bfs(grid, start)
end_distances = bfs(grid, end)
possible_cheats = {-2, 2, 2j, -2j}
if stage == 'b':
    for i in range(-20, 21):
        for j in range(21-abs(i)):
            possible_cheats.add(complex(i, j))
            possible_cheats.add(complex(i, -j))
for pos in list(grid.keys()):
    if grid[pos] == '.':  # try cheat
        for dir in possible_cheats:
            if grid[pos+dir] == '.' and start_distances[pos] + end_distances[pos+dir] + abs(dir.real) + abs(dir.imag) - start_distances[end] <= -100:
                result += 1

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
