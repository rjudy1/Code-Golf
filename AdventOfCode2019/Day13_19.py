# Advent of Code 2019 - Day 13

# Author:   Rachael Judy
# Date:     12/5/2020
# Purpose:  Game cabinet - break the blocks by bouncing ball on paddle
#               Check the comments with MOD to add the cheat wall for phase 2
#
# 0 - empty tile - white
# 1 - industructable wall - black
# 2 - block -  vermilion
# 3 - paddle - purple
# 4 - ball - green
#

import numpy as np
import pygame
import os, sys
import queue

import intcodecomputer
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# set this for part 1 or 2
phase = 2

# constants for displaying the game board
#                 R    G    B
BLACK =         (  0,   0,   0)
WHITE =         (255, 255, 255)
PURPLE =        (128,   0, 128)
VERMILION =     (227,  66,  51)
GREEN =         (  0, 204,   0)

colorDict = {0: WHITE, 1: BLACK, 2: VERMILION, 3: PURPLE, 4: GREEN}

# Create the constants for
BOARDWIDTH = 42  # number of columns in the board
BOARDHEIGHT = 24 # number of rows in the board
TILESIZE = 20
WINDOWWIDTH = 960
WINDOWHEIGHT = 640
FPS = 30

XMARGIN = int((WINDOWWIDTH - (TILESIZE * BOARDWIDTH + (BOARDWIDTH - 1))) / 2)
YMARGIN = int((WINDOWHEIGHT - (TILESIZE * BOARDHEIGHT + (BOARDHEIGHT - 1))) / 2)
global DISPLAYSURF


def drawBoard(board):
    DISPLAYSURF.fill(WHITE)

    for tilex in range(len(board)):
        for tiley in range(len(board[0])):
            if board[tilex][tiley]:
                drawTile(tilex, tiley, board[tilex][tiley])


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


# input
instructions = parseMod.readCSV('data/13game.csv')  # MODIFY TO 13gameMOD.csv for MOD VERSION

pygame.init()
FPSCLOCK = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Arcade Game')

# phase 1
if phase == 1:
    # create computer
    arcade = intcodecomputer.Computer(instructions)

    # run program and show gameboard
    count = 0
    inputQ = queue.SimpleQueue()
    gameboard = np.zeros((42, 24))
    output = arcade.processInput(inputQ)

    # process the output to show the board and count the block tiles
    for i in range(0, len(output), 3):
        gameboard[output[i], output[i+1]] = int(output[i+2])
        if output[i+2] == 2:  # count block tiles
            count += 1

    print("Block tiles: ", count)
    while True:
        drawBoard(gameboard)
        pygame.display.update()


# phase 2
else:
    bestScore = 0
    instructions[0] = 2
    # create computer
    arcade = intcodecomputer.Computer(instructions)

    # run program and show gameboard
    inputQ = queue.SimpleQueue()
    gameboard = np.zeros((44, 26))
    while not arcade.isDone():
        output = arcade.processInput(inputQ)

        # process the output to show the board
        for i in range(0, len(output), 3):
            if output[i] == -1 and output[i+1] == 0:
                print("Current Score: ", output[i+2])  # COMMENT IN TO SEE PROGRESS OF SCORE AS YOU GO
                bestScore = max(bestScore, output[i+2])
                break
            gameboard[output[i], output[i+1]] = int(output[i + 2])

        drawBoard(gameboard)

        # get input
        for event in pygame.event.get(): # event handling loop
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    inputQ.put(1)
                elif event.key == pygame.K_LEFT:
                    inputQ.put(-1)
                elif event.key == pygame.K_DOWN:
                    inputQ.put(0)
#        inputQ.put(0)  # COMMENT IN FOR MODIFIED WALL VERSION

        pygame.display.update()
        FPSCLOCK.tick(FPS)

    print("Best score: ", bestScore)