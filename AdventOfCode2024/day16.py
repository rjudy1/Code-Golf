# Advent of Code 2024 Day 16
# Author:   Rachael Judy
# Purpose:  djikstra, then dfs of cost map to find nodes on shortest paths

import collections
import csv
import math
import parseMod

ready = True
day = 16
stage = 'b'  # 130536, 1024
year = 2024

parseMod.createDataFile(year=year, day=day)
costs = collections.defaultdict(lambda: math.inf)
graph = collections.defaultdict(str)
with open("data/" + str(day).zfill(2) + "data.csv") as file:
    for i, row in enumerate(csv.reader(file)):
        for j, col in enumerate(row[0]):
            graph[complex(i, j)] = col
            if col == 'S':
                queue = collections.deque([(complex(i, j), 1j)])
                costs[(complex(i, j), 1j)] = 0

# djikstra to find least cost path to the end states
end_scores = collections.defaultdict(set)
while queue:
    position, dir = queue.popleft()
    if graph[position] == 'E':
        end_scores[costs[(position, dir)]].add((position, dir))
    if graph[position + dir] != '#' and costs[(position + dir, dir)] > costs[(position, dir)] + 1:  # move forward
        queue.append((position + dir, dir))
        costs[(position + dir, dir)] = costs[(position, dir)] + 1
    for turn in {1j, -1j}:
        if costs[(position, dir * turn)] > costs[(position, dir)] + 1000:  # turn right
            costs[(position, dir * turn)] = min(costs[(position, dir * turn)], costs[(position, dir)] + 1000)
            queue.append((position, dir * turn))

# dfs cost map from end, taking only paths with viable reductions, to find nodes on shortest paths
nodes_on_best_path = set()
if stage == 'b':
    def dfs(current_path):
        pos, dir = current_path[-1]
        if graph[pos] == 'S' and dir == 1j:  # if made it to start viably, add nodes to collection
            nodes_on_best_path.update({p for (p, d) in current_path})
            return
        if costs[pos - dir, dir] + 1 == costs[pos, dir]:  # step back
            current_path.append((pos - dir, dir))
            dfs(current_path)
            current_path.pop()
        for turn in {-1j, 1j}:
            if costs[pos, dir * turn] + 1000 == costs[pos, dir]:  # turn
                current_path.append((pos, dir * turn))
                dfs(current_path)
                current_path.pop()

    for end_state in end_scores[min(end_scores)]:
        dfs([end_state])

result = min(end_scores) if stage == 'a' else len(nodes_on_best_path)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
