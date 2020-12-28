# Advent of Code 2018 - Day 22

# Author:   Rachael Judy
# Date:     12/28/2020
# Purpose:  Build map of cave network and find shortest time to traverse path (Djikstra of weighted graph)

import networkx as nx

# your input HERE
depth = 6969
target = 9, 796

# makes map
grid = [[0 for _ in range(target[0]+100)] for _ in range(target[1] + 100)]  # 100 should be enough expansion
for y in range(len(grid)):
    for x in range(len(grid[0])):
        if y == 0:
            geo_index = x*16807
        elif x == 0:
            geo_index = y*48271
        elif x == target[0] and y == target[1]:  # at target
            geo_index = 0
        else:
            geo_index = grid[y-1][x] * grid[y][x-1]
        grid[y][x] = (geo_index + depth) % 20183  # erosion level
for y in range(len(grid)):
    for x in range(len(grid[0])):
        grid[y][x] = grid[y][x] % 3  # type and risk level

risk = sum(sum(row[:target[0]+1]) for row in grid[:target[1]+1])
print('part 1: ', risk)

torch, gear, neither = 0, 1, 2
valid_items = {0: (torch, gear), 1: (gear, neither), 2: (torch, neither)}

# build graph linking changing items and regions
graph = nx.Graph()
for y in range(len(grid)):
    for x in range(len(grid[0])):
        items = valid_items[grid[y][x]]
        graph.add_edge((x, y, items[0]), (x, y, items[1]), weight=7)  # cost to switch objects
        for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):  # every direction
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(grid[0]) and 0 <= new_y < len(grid):  # make link if objects held are compatible
                new_items = valid_items[grid[new_y][new_x]]
                for item in set(items).intersection(set(new_items)):
                    graph.add_edge((x, y, item), (new_x, new_y, item), weight=1)

print("part 2:", nx.dijkstra_path_length(graph, (0, 0, torch), (target[0], target[1], torch)))  # path mouth to target
