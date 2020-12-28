# Advent of Code 2018 - Day 20

# Author:   Rachael Judy
# Date:     12/28/2020
# Purpose:  Interpret input "regex" representing a map to a graph and find the shortest paths with most doors

import networkx as nx
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


paths = parseMod.readCSV_single('data/20regex.csv')[1:-1]  # read regex in as array

maze = nx.Graph()  # link positions accessible
pos = {0}  # the current positions that we're building on for the |
stack = []  # a stack keeping track of (starts, ends) for groups
starts, ends = {0}, set()  # current possible starting and ending positions

for c in paths:  # create graph
    if c == '|':  # an alternate: update possible ending points, and expand the group
        ends.update(pos)
        pos = starts
    elif c in ['N', 'E', 'S', 'W']:  # move in a given direction: add all edges and update our current positions
        direction = {'N': 1, 'E': 1j, 'S': -1, 'W': -1j}[c]
        maze.add_edges_from((p, p + direction) for p in pos)
        pos = {p + direction for p in pos}
    elif c == '(':  # start of group: add current positions as start of a new group
        stack.append((starts, ends))
        starts, ends = pos, set()
    elif c == ')':  # end of group: finish current group, add current positions as possible ends
        pos.update(ends)
        starts, ends = stack.pop()

# find the shortest path lengths from the starting room to all other rooms - makes dict of room, length  SSP
lengths = nx.algorithms.shortest_path_length(maze, 0)

print('part 1:', max(lengths.values()))  # farthest room by doors passed through
print('part 2:', sum(1 for length in lengths.values() if length >= 1000))  # number of paths where you pass through >=1k
