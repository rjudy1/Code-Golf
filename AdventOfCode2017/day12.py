# Advent of Code 2017 Day 12
# Author:   Rachael Judy
# Purpose:  connected components size and count

from collections import defaultdict, deque

import parseMod

ready = True
day = 12
stage = 'b'
year = 2017

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv")

# parse data to graph
adj = defaultdict(set)
for a, _, *rest in data:
    for b in rest:
        adj[int(a)].add(int(b.strip(',')))
        adj[int(b.strip(','))].add(int(a))


def bfs(start: int) -> None:
    queue = deque([start])
    while queue:
        node = queue.popleft()
        queue.extend(adj[node].difference(visited))
        visited.update(adj[node])


# size of group containing 0
visited = {0}  # global reuse in bfs
bfs(0)
cluster0_size = len(visited)

# count of groups
groups = 1
remaining = set(adj)-visited
while remaining:
    bfs(remaining.pop())
    groups += 1
    remaining -= visited

result = cluster0_size if stage == 'a' else groups

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
