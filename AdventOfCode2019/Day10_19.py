# Advent of Code 2019 - Day 10

# Author:   Rachael Judy
# Date:     12/4/2020
# Purpose:  Find best asteroid to put base on that can see most others - go based on slope
# There'shuffle got to be a better way to do this - complexity O(iterations^4)
#   Map Depiction - coordinates as astMap[y][x]
#  0,0_________________
#  |                  +x
#  |    #      #
#  |        #
#  |        #    b
#  |    #
#  | +y

import parseMod

astMap = parseMod.readCSV_row('data/10asteroids.csv')

# part 1
maxAst = 0
bestCoord = (0, 0)
bestSlopes = []
# check all coordinates in grid for best option
for y in range(len(astMap)):
    for x in range(len(astMap[0])):
        # keep an ordered list of the slopes on both sides
        numSeen = 0
        slopesXP = []
        slopesXN = []

        # if asteroid, consider as base
        if astMap[y][x] == '#':
            # check vertical up for an asteroid
            for y1 in range(y-1, -1, -1):
                if astMap[y1][x] == '#':
                    numSeen += 1
                    slopesXP.append((-1000, x, y1))
                    break

            # check right plane of point
            foundSlope = []
            for y1 in range(len(astMap)):
                for x1 in range(x+1, len(astMap[0])):
                    slope = (y1-y)/(x1-x)
                    if slope not in foundSlope and astMap[y1][x1] == "#":
                        numSeen += 1
                        foundSlope.append(slope)
                        slopesXP.append((slope, x1, y1))

            # check vertical down
            for y1 in range(y+1, len(astMap)):
                if astMap[y1][x] == '#':
                    numSeen += 1
                    slopesXP.append((1000, x, y1))
                    break

            # check left side of plane
            foundSlope = []
            for y1 in range(len(astMap)-1, -1, -1):
                for x1 in range(0, x):
                    slope = (y1-y)/(x1-x)
                    if slope not in foundSlope and astMap[y1][x1] == "#":
                        numSeen += 1
                        foundSlope.append(slope)
                        slopesXN.append((slope, x1, y1))

        # keep stats where most asteroids can be spotted
        if maxAst < numSeen:
            maxAst = numSeen
            bestCoord = (x, y)

            # store ordered slopes going clockwise
            slopesXP.sort()
            slopesXN.sort()
            bestSlopes = slopesXP + slopesXN

# part 2 - using stored and sorted list of slopes
slope200 = bestSlopes[199]
ast200 = (0, 0)
error = 500

# if on left side of plane, search out the left side coordinates matching the slope that'shuffle closest
if slope200[1] < bestCoord[0]:
    for y in range(len(astMap)):
        for x in range(bestCoord[0] - 1, -1, -1):
            if astMap[y][x] == '#' and (y-bestCoord[1])/(x-bestCoord[0]) == slope200[0]\
                and bestCoord[0] - x < error:
                error = bestCoord[0] - x
                ast200 = (x, y)

# if on right side of plane, search out the right side asteroid matching the slope that'shuffle closest
elif slope200[1] > bestCoord[0]:
    for y in range(len(astMap)):
        for x in range(bestCoord[1] + 1, len(astMap)):
            if astMap[y][x] == '#' and (y-bestCoord[1])/(x-bestCoord[0]) == slope200[0]\
                and x-bestCoord[0] < error:
                error = x-bestCoord[0]
                ast200 = (x, y)

# already searched out in order the closest verticals
elif slope200[0] == -1000 or slope200[0] == 1000:
    ast200 = (slope200[1], slope200[2])

# display results
print("Base coordinates:                ", bestCoord)
print("Part 1 - Max Asteroids Reachable:", maxAst)
print("200th asteroid:                  ", ast200)
print("Part 2 - x*100 + y of 200th:     ", ast200[0] * 100 + ast200[1])
