# Advent of Code 2019 - Day 20

# Author:   Rachael Judy
# Date:     12/13/2020
# Purpose:  Compute the number of steps through maze AA to ZZ - phase 1 portals direct connect to same lettering
#           - phase 2 portals on inside connect to a recursively nested maze to its outer ones
# NOTE - modified input txt to force it to read whitespace after last character on line - look at NOTE comments to use
#           on alternate maze - add a non . character to end of each line in the maze file so all lines are same length

import os
import sys
import networkx as nx  # this class is amazing

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# phase
phase = 2


# populates the portals dictionary with the points that hop between each portal
def add_portal(x, y):
    global portals, maze
    x_dot, y_dot = 0, 0  # address of the dot
    name = ''  # portal name

    # check if letter is to the right and associated dot is to the left or right
    if x + 1 < len(maze[0]) and maze[y][x + 1].isalpha():
        name = str(maze[y][x]) + str(maze[y][x + 1])  # get name letters
        if x+2 < len(maze) and maze[y][x+2] == '.':  # is to the right
            x_dot = x+2
            y_dot = y
        else:  # is to the left
            x_dot = x-1
            y_dot = y

    # check up and down for letters
    elif y + 1 < len(maze) and maze[y+1][x].isalpha():
        name = str(maze[y][x]) + str(maze[y+1][x])
        if y+2 < len(maze) and maze[y+2][x] == '.':  # down
            x_dot = x
            y_dot = y + 2
        else:  # up
            x_dot = x
            y_dot = y - 1

    # if this portal point has not been found, add it to the dictionary
    if len(name) == 2 and name in portals and len(portals[name]) < 2 and portals[name][0] != (x_dot, y_dot):
        portals[name].append((x_dot, y_dot))
    elif len(name) == 2 and name not in portals:  # if no dictionary entry for this name yet
        portals[name] = []
        portals[name].append((x_dot, y_dot))


# read in as grid - using the modded input
global maze, portals
maze = parseMod.readCSV_row('data/20maze.txt', '\n')

# phase 1 - portals jump to each other directly - virtually identical to part 2 with the addition of layering
if phase == 1:
    G = nx.Graph()
    portals = {}  # key will be name, will have list of two children for locations of portal

    # go through maze and collect the useful points, populate the graph
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == '.':
                G.add_node((x, y))  # add self

                if x+1 < len(maze[0]) and maze[y][x+1] == '.':  # check right
                    G.add_edge((x, y), (x+1,y))

                if x-1 >= 0 and maze[y][x-1] == '.':  # check left
                    G.add_edge((x, y), (x-1, y))

                if y+1 < len(maze) and maze[y+1][x] == '.':  # check down
                    G.add_edge((x, y), (x, y+1))

                if y-1 >= 0 and maze[y-1][x] == '.':  # check up
                    G.add_edge((x, y), (x, y-1))

            elif char.isalpha():  # check if portal already labeled
                add_portal(x, y)

    # add the portal edges to the graph
    for name in portals:
        if len(portals[name]) == 2:  # not start or finish
            G.add_edge(portals[name][0], portals[name][1])

    # save start and finish points
    start = portals['AA'][0]
    finish = portals['ZZ'][0]

    # use nx shortest_path to find between start and finish
    shortest_path = nx.shortest_path(G, start, finish)
    print("PART 1")
    print("Path: ", shortest_path)
    print("Length: ", len(shortest_path) - 1)  # node sea_monster_count, subtract one for start

# part 2
else:
    G = nx.Graph()
    portals = {}  # key will be name, will have list of two children for ends of portal

    # populate maze - same as part 1 but with addition of layers
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            for layer in range(35):  # create 35 layers of nodes - each node has extra layer
                if char == '.':
                    G.add_node((x, y, layer))

                    if x+1 < len(maze[0]) and maze[y][x+1] == '.':
                        G.add_edge((x, y, layer), (x+1, y, layer))
                    if x-1 >= 0 and maze[y][x-1] == '.':
                        G.add_edge((x, y, layer), (x-1, y, layer))
                    if y+1 < len(maze) and maze[y+1][x] == '.':
                        G.add_edge((x, y, layer), (x, y+1, layer))
                    if y-1 >= 0 and maze[y-1][x] == '.':
                        G.add_edge((x, y, layer), (x, y-1, layer))

                elif char.isalpha():
                    add_portal(x, y)

    # create the portal linkages between layers
    for name in portals:
        if len(portals[name]) == 2:
            # upper bound might need to be adjusted for different size mazes - capture the middle in the bounds
            # first point in middle of maze goes to next layer
            if 3 < portals[name][0][0] < 100 and 3 < portals[name][0][1] < 100:
                i = 0  # layer of first  (added to k)
                j = 1  # layer of second (added to k)
            else:
                i = 1
                j = 0

            # add each layer link from in to out of nested - layer 34 technically not connected to further inner layers
            for k in range(34):
                G.add_edge((portals[name][0][0], portals[name][0][1], i+k),
                           (portals[name][1][0], portals[name][1][1], j+k))

    # store start points on layer 0
    start = (portals['AA'][0][0], portals['AA'][0][1], 0)
    finish = (portals['ZZ'][0][0], portals['ZZ'][0][1], 0)

    # compute shortest path
    shortest_path = nx.shortest_path(G, start, finish)
    print("PART 2")
    print("Path: ", shortest_path)
    print("Length: ", len(shortest_path) - 1)
