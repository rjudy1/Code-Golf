# Advent of Code 2024 Day 18
# Author:   Rachael Judy
# Purpose:  bfs the increasingly dangerous maze

import collections
import csv
import parseMod

ready = True
day = 18
stage = 'b'
year = 2024

parseMod.createDataFile(year=year, day=day)
grid = collections.defaultdict(int)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    limit = 70  # upper boundary
    for i, row in enumerate(reader):
        a, b = map(int, row)
        grid[complex(a, b)] = 1
        if i < 1023:  # know of path through here at least
            continue

        reached = False
        queue = collections.deque([(0, 0)])
        visited = set()
        while queue and not reached:
            pos, steps = queue.popleft()
            if pos == (limit+limit*1j):
                reached = True
            for dir in {1, -1, 1j, -1j}:
                if 0 <= (pos+dir).real <= limit and 0 <= (pos+dir).imag <= limit and pos + dir not in visited and grid[pos+dir] == 0:
                    queue.append((pos+dir, steps+1))
                    visited.add(pos+dir)

        if stage == 'a':
            result = steps
            break
        if not reached:
            result = ','.join(row)
            break

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
