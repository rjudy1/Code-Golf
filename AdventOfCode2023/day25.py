# Advent of Code 2023 Day 25
# Author:   Rachael Judy
# Date:     12/25/23
# Purpose:  Find three connections to cut that split the ports into two groups, visualize with graphviz


import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'

from collections import deque, defaultdict
import graphviz
from heapq import nlargest
import parseMod

ready = True
day = 25
stage = 'a'
year = 2023

parseMod.createDataFile(year=year, day=day)
data = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")

connections = defaultdict(set)
dot = graphviz.Graph()  # for visualization and checking grouping, not necessary for solve
for row in data:
    a, b = row.split(': ')[0], row.split(': ')[1].split(' ')
    connections[a].update(b)
    for port in b:
        dot.edge(a, port)
        connections[port].add(a)
dot.view()  # view graph that was built

# do a bfs to find shortest path to each node from each node and count most frequent connections
usage_count = defaultdict(lambda: 0)
for node in connections:
    q, visited, parent_dict = deque([node]), {node}, dict()
    while q:  # bfs tracking parents
        val = q.popleft()
        for n in connections[val].difference(visited):
            parent_dict[n] = val
            q.append(n)
        visited.update(connections[val])
    for n in connections:  # backup parents counting use of each connection from each node
        pos = n
        while pos != node:
            usage_count[tuple(sorted([pos, parent_dict[pos]]))] += 1
            pos = parent_dict[pos]

best_pairs = res = nlargest(3, usage_count, key=usage_count.get)  # most frequently used connections would be critical 3
for a, b in best_pairs:
    connections[a].discard(b)
    connections[b].discard(a)

# bfs from one side after cutting connections to find count on side of line
q1 = deque([best_pairs[0][0]])
visited_1 = {best_pairs[0][0]}
while q1:
    top = q1.popleft()
    q1.extend(connections[top].difference(visited_1))
    visited_1.update(connections[top])
result = len(visited_1) * (len(connections) - len(visited_1))

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)