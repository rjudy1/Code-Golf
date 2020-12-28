# Advent of Code 2018 - Day 25

# Author:   Rachael Judy (c) rjudy1
# Date:     12/28/20
# Purpose:  Count constellations formed by stars less than 3 Manhattan from others in their group

import networkx as nx
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

stars = parseMod.readCSV_row('data/25stars.csv')
for i, line in enumerate(stars):
    stars[i] = tuple(int(x) for x in line.split(','))

# build graph with edges meeting conditions, get number of connected components
manhattan = lambda a, b: sum(abs(x - y) for x, y in zip(a, b))  # function returns manhattan dist
constellations = nx.Graph()
for star1 in stars:
    for star2 in stars:
        if manhattan(star1, star2) <= 3:
            constellations.add_edge(star1, star2)
print("Constellations: ", (nx.number_connected_components(constellations)))