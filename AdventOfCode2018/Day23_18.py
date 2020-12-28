# Advent of Code 2018 - Day 23

# Author:   Rachael Judy (c) rjudy1
# Date:     12/28/20
# Purpose:  3d manhattan spheres in space - find number inside biggest sphere and closest point in max number of spheres

import networkx as nx
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# parse input into tuples
inp = parseMod.readCSV_row('data/23drones.csv')
bots = []
for line in inp:
    line = line.split(',')
    bots.append((int(line[0][5:]), int(line[1]), int(line[2].strip('>')), int(line[3][3:])))

X, Y, Z, RADIUS = 0, 1, 2, 3
ORIGIN = (0, 0, 0, 0)
manhattan = lambda a, b: abs(a[X] - b[X]) + abs(a[Y] - b[Y]) + abs(a[Z] - b[Z])  # function returns manhattan dist

# part 1
largest_radius_bot = max(bots, key=lambda bot: bot[RADIUS])
print('part 1:', sum((manhattan(largest_radius_bot, bot) <= largest_radius_bot[RADIUS]) for bot in bots))

# part 2
# build a graph with edges between overlapping nanobots
graph = nx.Graph()
for bot in bots:
    # two bots overlap if their distance is smaller or equal than the sum of their ranges
    overlaps = [(bot, other) for other in bots if manhattan(bot, other) <= bot[RADIUS] + other[RADIUS]]
    graph.add_edges_from(overlaps)

# find sets of overlapping nanobots (i.e. fully-connected sub-graphs)
cliques = list(nx.find_cliques(graph))
cliques_size = [len(c) for c in cliques]
assert len([s for s in cliques_size if s == max(cliques_size)]) == 1  # currently no tie breaking check so make sure it doesn't matter
clique = max(cliques, key=len)  # keep largest clique

# calculate the point in the nanobots' radii which is closest to the origin - greedy strategy - not confident as general
points = [manhattan(ORIGIN, bot) - bot[RADIUS] for bot in clique]
# furthest away point in points needed to get all bots in the clique but closest to origin
print('part 2:', max(points))
