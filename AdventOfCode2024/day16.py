# Advent of Code 2024 Day 16
# Author:   Rachael Judy
# Purpose:  djikstra plus tracking of multiple possible best paths
# so slow with the repeated search, clean this up

import collections
import csv
import math
import parseMod

ready = True
day = 16
stage = 'b'
year = 2024

parseMod.createDataFile(year=year, day=day)
costs = collections.defaultdict(lambda: math.inf)
map = collections.defaultdict(str)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        for j, col in enumerate(row[0]):
            map[complex(i,j)] = col
            if col == 'S':
                queue = collections.deque([(complex(i,j), 1j)])
                costs[(complex(i,j), 1j)] = 0

# bfs (no early termination?)
directions = {1j, -1, -1j, 1}
# visited = set()  # position, direction
end_scores = set()

while queue:
    # rotation will be multiplication by j or -j
    position, dir = queue.popleft()
    if map[position] == 'E':
        end_scores.add(costs[(position,dir)])
    if map[position + dir] != '#' and costs[(position+dir, dir)] > costs[(position, dir)]+1: #  not referencing visited?
        # visited.add((position+dir, dir))
        queue.append((position+dir, dir))
        costs[(position+dir, dir)] = costs[(position, dir)]+1
    if costs[(position, dir*1j)] > costs[(position, dir)]+1000:
        # visited.add((position, dir*1j))
        costs[(position, dir*1j)] = min(costs[(position, dir*1j)], costs[(position, dir)]+1000)
        queue.append((position, dir*1j))
    if costs[(position, dir*-1j)] > costs[(position, dir)]+1000:
        # visited.add((position, dir*-1j))
        costs[(position, dir*-1j)] = min(costs[(position, dir*-1j)], costs[(position, dir)]+1000)
        queue.append((position, dir*-1j))

print(end_scores)
result = min(end_scores)

# retrace best path(s)
# start from end and walk backward (anytime score goes down?)
# iterate all paths without the adjustment and see which ones lead to the min score

on_path = set()
for (pos, dir) in costs:
    if costs[(pos,dir)] > result:
        continue
    # check if this will be on the best path
    queue = collections.deque([(pos,dir)])
    new_costs = collections.defaultdict(lambda: math.inf)
    new_costs[(pos,dir)] = costs[(pos, dir)]
    end_scores = set()

    while queue:
        # rotation will be multiplication by j or -j
        position, dir = queue.popleft()
        if map[position] == 'E':
            end_scores.add(new_costs[(position, dir)])
        if map[position + dir] != '#' and new_costs[(position + dir, dir)] > new_costs[
            (position, dir)] + 1 and new_costs[(position, dir)] + 1 <= result:  # not referencing visited?
            # visited.add((position+dir, dir))
            queue.append((position + dir, dir))
            new_costs[(position + dir, dir)] = new_costs[(position, dir)] + 1
        if map[position + dir*1j] != '#' and new_costs[(position, dir * 1j)] > new_costs[(position, dir)] + 1000 and new_costs[(position, dir)] + 1000 <= result:
            # visited.add((position, dir*1j))
            new_costs[(position, dir * 1j)] = min(new_costs[(position, dir * 1j)], new_costs[(position, dir)] + 1000)
            queue.append((position, dir * 1j))
        if map[position + dir*-1j] != '#' and new_costs[(position, dir * -1j)] > new_costs[(position, dir)] + 1000 and new_costs[(position, dir)] + 1000 <= result:
            # visited.add((position, dir*-1j))
            new_costs[(position, dir * -1j)] = min(new_costs[(position, dir * -1j)], new_costs[(position, dir)] + 1000)
            queue.append((position, dir * -1j))
    print(len(on_path))
    if end_scores and min(end_scores) == result:
        on_path.add(pos)
result = len(on_path)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
