# Advent of Code 2019 - Day 14

# Author:   Rachael Judy
# Date:     12/7/2020
# Purpose:  Determine how many input ORE to produce an output of FUEL and how much can be produced by 1 trillion ORE


import math
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


# calculate the amount of each element to determine the amount of ORE needed
# fills out the targetCosts recursively
# param: target is tuple of (element, amount)
# amountsNeeded has key name and value [using, spare]
def calculateCost(target):
    global reactionDict, amountsNeeded, outputDict  # dictionary of equation representations,
                                                    # amounts needed, output quantity for reactions
    if target[0] == 'X':  # end of reactions
        return

    # compute reactions needed, amount generated, and new amount of leftover items
    reactionsNeeded = math.ceil((target[1] - amountsNeeded[target[0]][1]) / outputDict[target[0]])
    generated = reactionsNeeded * outputDict[target[0]]
    spare = generated - target[1] + amountsNeeded[target[0]][1]

    # assign amount needed and spare for the target
    amountsNeeded[target[0]][0] += generated  # target number used
    amountsNeeded[target[0]][1] = spare  # spares

    # check the needs of all children elements
    for element in reactionDict[target[0]]:
        elementsNeeded = reactionsNeeded * element[1]  # number of element needed to produce target
        calculateCost((element[0], elementsNeeded))  # call on element to find out if extra generated and get children


# parse input
reactions = parseMod.readCSV_rowEl('data/14reactions.csv')
global reactionDict, amountsNeeded, outputDict  # dictionary of equation represenations and costs

reactionDict = dict()
outputDict = dict()
amountsNeeded = dict()

# parse into output input dictionaries
for reaction in reactions:
    inputs = []
    for i in range(0, len(reaction) - 3, 2):
        inputs.append((reaction[i+1].strip(','), int(reaction[i])))

    reactionDict[reaction[-1]] = inputs
    outputDict[reaction[-1]] = int(reaction[-2])

# set up break condition
outputDict['ORE'] = 1
reactionDict['ORE'] = [('X', 0)]

for reaction in reactionDict.keys():
    amountsNeeded[reaction] = [0, 0]

# find number of ore to get ('FUEL', 1)
target = 'FUEL', 1
calculateCost(target)

# part 1
orePerFuel = amountsNeeded['ORE'][0]
print("ORE needed per FUEL: ", orePerFuel)


# part 2
# reset and recalculate - a little sketchy ratio method that worked as well as the range based loop and confirm
goal = 1000000000000

# check on possible combos (process of elimination via exp for range)
for i in range(1639300, 1639400):
    for reaction in reactionDict.keys():
        amountsNeeded[reaction] = [0, 0]
    calculateCost(('FUEL', i))

    # exit loop if needs more than available, store last acceptable fuel occupied_count
    if amountsNeeded['ORE'][0] >= goal:
        fuelCount = i - 1
        break

print("Maximum FUEL: ", fuelCount)

# # slightly sketchy solution, works
# # ratio of available to amount used to generate individual FUELs - works because of huge numbers
# for reaction in reactionDict.keys():  # reset
#     amountsNeeded[reaction] = [0, 0]
# calculateCost(('FUEL', int(goal / orePerFuel)))
# oreCost = amountsNeeded['ORE'][0]
# fuelCount = int(int(goal / orePerFuel) * (goal / oreCost))
