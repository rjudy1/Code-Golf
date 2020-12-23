# Advent of Code 2019 - Day 18

# Author:   Rachael Judy
# Date:     12/12/2020
# Purpose:  Compute the least number of steps from entrance to collect all keys
#

import os
import sys

from collections import defaultdict, namedtuple, deque
import networkx as nx
from itertools import combinations
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


Point = namedtuple('P', 'x y')


# Path class to track optimal
class Path:
    def __init__(self, current, collected_keys, length):
        self.current = current
        self.collected_keys = collected_keys
        self.length = length

    def get_state(self):
        unique_state = (self.current, self.collected_keys)
        return unique_state

    def path_length(self):  # bitmap
        return bin(self.collected_keys).count("1")

    def __repr__(self):  # display
        return str(self.current) + " " + str(bin(self.collected_keys)) + " : " + str(self.length)


# get the grid from the input file
def get_grid(part_b=False):
    grid = defaultdict(int)
    keys = {}
    doors = {}
    start_points = []

    # read input
    lines = parseMod.readCSV_row('data/18maze.csv')
    for row in range(len(lines)):
        temp = []
        for item in lines[row]:
            temp.append(item)
        lines[row] = temp

    mid_y = (len(lines) - 1) // 2  # find the center
    mid_x = (len(lines[0]) - 1) // 2
    if part_b:  # if part B, modify the input
        lines[mid_y - 1][mid_x - 1:mid_x + 2] = "@#@"
        lines[mid_y][mid_x - 1:mid_x + 2] = "###"
        lines[mid_y + 1][mid_x - 1:mid_x + 2] = "@#@"

    for y, line in enumerate(lines):
        for x, c in enumerate(line):  # go through each character in i, add position and item to point if not wall
            if c != '#':
                p = Point(x, y)
                grid[p] = 1
                if c == '@':
                    start_points.append(p)
                elif c != '.':
                    o = ord(c)
                    if o >= 97:
                        keys[o - 97] = p
                    else:
                        doors[o - 65] = p

    # track locations
    total_start_points = len(start_points)
    keys = {k + total_start_points: v for k, v in keys.items()}
    doors = {k + total_start_points: v for k, v in doors.items()}

    return grid, keys, doors, start_points, x, y


def get_surrounding_points(p):
    return set([
        Point(p.x, p.y - 1),
        Point(p.x, p.y + 1),
        Point(p.x - 1, p.y),
        Point(p.x + 1, p.y),
    ])


# create the graph from the edges in the grid
def build_graph(grid, max_x, max_y):
    edges = []
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            p = Point(x, y)
            if grid[p]:
                for sp in get_surrounding_points(p):
                    if grid[sp]:
                        edges.append((p, sp))
    return nx.Graph(edges)  # uses nx for graph operations


# use networkx built graph to find shortest between 2 points
def get_distance(G, p0, p1, doors):
    if not nx.has_path(G, p0, p1):  # if there is no path
        return None
    path = nx.shortest_path(G, p0, p1)  # compute shortest path - use networkx cap
    path_set = set(path)
    doors_in_way = 0
    for k, p in doors.items():
        if p in path_set:
            doors_in_way += (1 << k)  # track if doors are on path
    distance = len(path) - 1
    return distance, doors_in_way


# creates a dictionary of paths key to key
def get_key_to_key(G, keys, doors, start_points, start_points_nums):
    key_to_key = defaultdict(dict)

    key_to_bits = {k: 1 << k for k in keys.keys()}

    # check start to each key
    for start_point, start_point_num in zip(start_points, start_points_nums):
        start_point_bits = 1 << start_point_num
        for k, p in keys.items():
            k_bits = key_to_bits[k]
            res = get_distance(G, start_point, p, doors)
            if res is not None:
                distance, doors_in_way = res  # track obstructing doors
                key_to_key[start_point_bits][k_bits] = (distance, doors_in_way)

    # check each key location to others
    for k0, k1 in combinations(keys.keys(), 2):
        k0_bits = key_to_bits[k0]
        k1_bits = key_to_bits[k1]

        res = get_distance(G, keys[k0], keys[k1], doors)
        if res is not None:
            distance, doors_in_way = res
            key_to_key[k0_bits][k1_bits] = (distance, doors_in_way)
            key_to_key[k1_bits][k0_bits] = (distance, doors_in_way)

    return dict(key_to_key)


# kind of excessive, but computes next possible along path, yielding if blocked
def find_next_possible_paths(key_to_key, path):
    current_positions = path.current
    for k0, v0 in key_to_key.items():
        if k0 & current_positions:
            for k1, v1 in v0.items():
                if not k1 & path.collected_keys:
                    dist, doors_in_way = v1
                    if doors_in_way & path.collected_keys == doors_in_way:
                        new_position = current_positions ^ k0 | k1
                        yield Path(new_position, path.collected_keys + k1, path.length + dist)


# builds graph, and finds SP
def find_smallest_path(grid, keys, doors, start_points, max_x, max_y):
    G = build_graph(grid, max_x, max_y)

    total_keys = len(keys)
    start_points_nums = list(range(len(start_points)))
    start_points_bits = int(np.bitwise_or.reduce(list(map(lambda x: 1 << x, start_points_nums))))

    key_to_key = get_key_to_key(G, keys, doors, start_points, start_points_nums)
    full_paths = []
    start_path = Path(start_points_bits, 0, 0)

    # keep shortest path
    min_full_path_length = 1000000000000
    min_path_lengths = defaultdict(int)

    # go through the possibel paths
    counter = 0
    possible_paths = deque([start_path])
    while possible_paths:
        counter += 1
        path = possible_paths.popleft()

        # if not a new possible min
        if min_path_lengths[path.get_state()] < path.length:
            continue

        # check next possible path, updating state
        for new_path in find_next_possible_paths(key_to_key, path):
            if new_path.length < min_full_path_length:
                unique_state = new_path.get_state()
                better_path = False
                if unique_state in min_path_lengths:  # if a new iteration
                    if new_path.length < min_path_lengths[unique_state]:
                        min_path_lengths[unique_state] = new_path.length
                        better_path = True
                else:
                    min_path_lengths[unique_state] = new_path.length
                    better_path = True

                # if a better path was found, add it to the possibilities
                if better_path:
                    if new_path.path_length() == total_keys:
                        if new_path.length < min_full_path_length:
                            min_full_path_length = new_path.length

                        full_paths.append(new_path)
                    else:
                        possible_paths.append(new_path)

    # return the minimum path
    return min([p.length for p in full_paths]), counter


# Part A
grid, keys, doors, start_points, max_x, max_y = get_grid()
min_length, counter = find_smallest_path(grid, keys, doors, start_points, max_x, max_y)

print("Part 1 Min path length:", min_length)
print("Iterations:", counter)
print()


# Part B - same but with four robots and slightly modded input
grid, keys, doors, start_points, max_x, max_y = get_grid(part_b=True)
min_length, counter = find_smallest_path(grid, keys, doors, start_points, max_x, max_y)

print("Part 2 min path length: ", min_length)
print("Iterations:", counter)
