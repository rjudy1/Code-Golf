# Advent of Code 2024 Day 18
# Author:   Rachael Judy
# Purpose:  bfs the increasingly dangerous maze

import collections
import csv
import parseMod

ready = True
day = 18
stage = 'b'  # 302, (24,32)
year = 2024

parseMod.createDataFile(year=year, day=day)
corrupted_coords = list()
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    for i, row in enumerate(csv.reader(file)):
        corrupted_coords.append(complex(*map(int, row)))


def bfs(limit, obstacles):  # always starts at (0,0) and tries to get to (limit, limit)
    queue, visited = collections.deque([(0, 0)]), set()
    while queue:
        pos, steps = queue.popleft()
        if pos == (limit+limit*1j):
            return steps
        for dir in {1, -1, 1j, -1j}:
            if 0 <= (pos+dir).real <= limit and 0 <= (pos+dir).imag <= limit and pos + dir not in visited and pos+dir not in obstacles:
                queue.append((pos+dir, steps+1))
                visited.add(pos+dir)
    return -1


lower_bound, upper_bound = 1024, len(corrupted_coords) - 1
while lower_bound < upper_bound-1:  # loop until breaking point found with binary search, assume exists
    cut_point = (lower_bound + upper_bound) // 2
    if bfs(70, set(corrupted_coords[:cut_point])) > 0:  # still possible to route
        lower_bound = cut_point
    else:
        upper_bound = cut_point
result = bfs(70, set(corrupted_coords[:1024])) if stage=='a' else str(int(corrupted_coords[lower_bound].real)) + ',' + str(int(corrupted_coords[lower_bound].imag))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
