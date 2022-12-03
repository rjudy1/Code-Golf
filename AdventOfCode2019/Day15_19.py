# Advent of Code 2019 - Day 15

# Author:   Rachael Judy
# Date:     12/8/2020
# Purpose:  Find path to oxygen control and longest path - uses depth first search (DFS) of paths
#           Scroll to bottom and comment/uncomment the indicated code to use the visualization

import os
import queue
import sys

import intcodecomputer
import numpy as np
import pygame
import copy

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


# associates Location with each coordinate pair for mapping
class Location:
    def __init__(self, coordinates):
        self.coords = coordinates
        x = coordinates[0]
        y = coordinates[1]
        self.pred = None
        self.direction = [3, 4, 2, 1]
        self.children = [(x-1, y), (x+1, y), (x, y+1), (x, y-1)]
        self.color = 'W'
        self.time = 0


# store time
global time
time = 0
# recursively used for DFS
def DFS_Visit(location, robot, depth):
    global time
    time = time + 1

    # store start time and color the working vertex gray
    location_dict[location].time = time
    location_dict[location].color = 'G'

    inputQ = queue.SimpleQueue()
    # go through adjacencies and store predecessors, follow recursively
    for loca, dire in zip(location_dict[location].children, location_dict[location].direction):
        if location_dict[loca].color == 'W':  # if undiscovered
            # check directions
            inputQ.put(dire)
            output = robot.processInput(inputQ)[0]

            if output == 1 or output == 2:  # if the robot did move, follow that path
                location_dict[loca].pred = location  # save predecessor
                if output == 2:  # save the oxygen location for 1 and the robot state (its position) for part 2
                    global oxygenLocation
                    oxygenLocation = loca
                    global robotCopy
                    robotCopy = copy.deepcopy(robot)
                    global oxDepth
                    oxDepth = depth + 1  # looking at adjacencies of the one in focus so add one

                # search depth
                DFS_Visit(loca, robot, depth+1)

                # back up
                if dire == 1 or dire == 2:
                    inputQ.put(3 - dire)
                elif dire == 3 or dire == 4:
                    inputQ.put(7 - dire)
                robot.processInput(inputQ)

    # color completed vertices
    location_dict[location].color = 'B'

    # record max depth
    global maxDepth
    maxDepth = max(maxDepth, depth)  # depth at bottom


# input
instructions = parseMod.readCSVInts('data/15droid.csv')

# create computer
robot = intcodecomputer.Computer(instructions)

# run program
grid = np.zeros((100, 100))
x, y = 50, 50  # start at center

### COMMENT TO THE END COMMENT NOTE FOR VISUALIZATION
# set location dictionary up - not needed to be global, but saves some parameter passing
global location_dict
location_dict = dict()
global oxygenLocation, maxOx, maxDepth, robotCopy
maxOx, maxDepth = 0, 0
for x in range(len(grid)):
    for y in range(len(grid)):
        location_dict[(x, y)] = Location((x, y))

# visit depth first
DFS_Visit((50, 50), robot, 0)
print("Oxygen Location: ", oxygenLocation)

# print ox distance as saved - alternate method used was to follow back the predecessor from the saved coordinates
print("Oxygen distance: ", oxDepth)

# part 2
# saved state from first search for robot placement
# reset location dictionary for reuse (could pass it instead of globaling but whatever)
for x in range(len(grid)):
    for y in range(len(grid)):
        location_dict[(x, y)] = Location((x, y))

# do DFS from oxygen
DFS_Visit(oxygenLocation, robotCopy, 0)

# show maxDepth found from the oxygen plunge
print("Longest path: ", maxDepth)
################ COMMENT WHAT'S BETWEEN THE INDICATED ### THIS IS END POINT


### VISUALIZATION TOOLS - Uncomment the bottom stuff and comment the search if you want to use it
# ignore the visualization stuff unless you want to use the visualizer
# constants for displaying the game board
#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
PURPLE =        (128,   0, 128)
VERMILION =     (227,  66,  51)
GREEN =         (  0, 204,   0)

colorDict = {1: WHITE, 0: BLACK, 2: VERMILION, 3: PURPLE, 4: GREEN}

# Create the constants for
BOARDWIDTH = 100   # number of columns in the board
BOARDHEIGHT = 100  # number of rows in the board
TILESIZE = 10
WINDOWWIDTH = 1000
WINDOWHEIGHT = 600
FPS = 30

XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
global DISPLAYSURF


def drawBoard(board):
    DISPLAYSURF.fill(GREEN)

    for tiley in range(len(board)):
        for tilex in range(len(board[0])):

            drawTile(tilex, tiley, board[tiley][tilex])


def getLeftTopOfTile(tileX, tileY):
    left = XMARGIN + (tileX * TILESIZE) + (tileX - 1)
    top = YMARGIN + (tileY * TILESIZE) + (tileY - 1)
    return (left, top)


def drawTile(tilex, tiley, number, adjx=0, adjy=0):
    # draw a tile at board coordinates tilex and tiley, optionally a few
    # pixels over (determined by adjx and adjy)
    TILECOLOR = colorDict[number]
    left, top = getLeftTopOfTile(tilex, tiley)
    pygame.draw.rect(DISPLAYSURF, TILECOLOR, (left + adjx, top + adjy, TILESIZE, TILESIZE))

## for the visualization
# pygame.init()
# FPSCLOCK = pygame.time.Clock()
# DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
# pygame.display.set_caption('Maze Buildup')
#
## self exploration visual
# inputQ = queue.SimpleQueue()
# grid[y, x] = 3  # the robot
# while not robot.isDone():
#     output = robot.processInput(inputQ)
#
#     # process the output to show the board
#     for i in range(0, len(output)):
#         grid[y, x] = 1
#         if direction == 'U':
#             grid[y-1, x] = output[i]
#             y -= (output[i] == 1 or output[i] == 2)
#         elif direction == 'D':
#             grid[y+1, x] = output[i]
#             y += (output[i] == 1 or output[i] == 2)
#         elif direction == 'L':
#             grid[y, x - 1] = output[i]
#             x -= (output[i] == 1 or output[i] == 2)
#         elif direction == 'R':
#             grid[y, x + 1] = output[i]
#             x += (output[i] == 1 or output[i] == 2)
#         grid[50, 50] = 4
#         print(x, y)
#         if output[i] == 2:
#             print("SOLVED", x, y)
#         else:
#             grid[y, x] = 3
#
#     for event in pygame.event.get():  # event handling loop
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 direction = 'R'
#                 inputQ.put(3)
#             elif event.key == pygame.K_LEFT:
#                 direction = 'L'
#                 inputQ.put(4)
#             elif event.key == pygame.K_DOWN:
#                 direction = 'D'
#                 inputQ.put(2)
#             elif event.key == pygame.K_UP:
#                 direction = 'U'
#                 inputQ.put(1)
#
#     drawBoard(grid)
#     pygame.display.update()
#     FPSCLOCK.tick(FPS)
