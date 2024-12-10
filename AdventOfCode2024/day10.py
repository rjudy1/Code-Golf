# Advent of Code 2024 Day 10
# Author:   Rachael Judy
# Purpose:  score of each trailhead (number of peaks reached) summed, then number of unique paths
# alternate approach: BFS but instead of including source in the node of the graph, keep track of paths that could lead
#                       to every node/sources that lead to the node in dict this ended up being faster (because the
#                       number of sources is no longer multiplied in the time complexity) but requiring more storage and
#                       was less clean
import collections
import csv
import parseMod

ready = True
day = 10
stage = 'b'  # 531, 1210
year = 2024

parseMod.createDataFile(year=year, day=day)
trail_map = dict()
queue = collections.deque()
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    reader = csv.reader(file)
    for i, row in enumerate(reader):
        for j, col in enumerate(row[0]):
            trail_map[complex(i, j)] = int(col)
            if col == '0':  # grab the trailheads
                queue.append((complex(i, j), complex(i, j)))

import time
start = time.time()
# .013, .007
# .008, .015
result = 0
if stage == 'a':
    visited = collections.defaultdict(set)
elif stage == 'b':
    visited = collections.defaultdict(int)
    for val in queue:
        visited[val[0]] = 1
    # queue = collections.deque([node for node,source in queue])
directions = [1, 1j, -1, -1j]
while queue:
    node, source = queue.popleft()
    for dir in directions:
        if node+dir in trail_map and trail_map[node] + 1 == trail_map[node+dir]: # and (stage == 'b' or (node+dir, source) not in visited):
            if stage == 'a':
                visited[node+dir].add(source)
                queue.append((node + dir,source))
            else:
                if visited[node + dir] == 0:
                    queue.append((node+dir, source))
                visited[node+dir] += visited[node]
for node in visited:
    if trail_map[node] == 9:
        result += visited[node] if stage == 'b' else len(visited[node])

# bfs from each trailhead, counting endpoints from each source/trails from each source
# result = 0
# visited = set()
# directions = [1, 1j, -1, -1j]
# while queue:
#     node, source = queue.popleft()
#     for dir in directions:
#         if node+dir in trail_map and trail_map[node] + 1 == trail_map[node+dir] and (stage == 'b' or (node+dir, source) not in visited):
#             queue.append((node+dir, source))
#             visited.add((node+dir, source))
#             if trail_map[node+dir] == 9:
#                 result += 1
print(time.time()-start)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
