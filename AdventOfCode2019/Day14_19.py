# Advent of Code 2019 - Day 14

# Author:   Rachael Judy
# Date:     12/6/2020
# Purpose:  Determine how many input ORE to produce an output of FUEL
# WORK IN PROGRESS

import math
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

def calculateCost(target, chemicalDict, outputDict, needed):
    temp = 0
    cost = 0
    for chemR in chemicalDict[target[0]]:
        if chemR[0] != 'ORE':
            cost += math.ceil(chemR[1] / outputDict[chemR[0]] * calculateCost(chemR, chemicalDict, outputDict, needed))
        else:
            return chemR[1]

    return cost


reactions = parseMod.readCSV_rowEl('data/14reactions.csv')

chemicalDict = dict()
outputDict = dict()
for reaction in reactions:
    inputs = []
    for i in range(0, len(reaction) - 3, 2):
        inputs.append((reaction[i+1].strip(','), int(reaction[i])))

    chemicalDict[reaction[-1]] = inputs
    outputDict[reaction[-1]] = int(reaction[-2])
outputDict['ORE'] = 1
# find number of ore to get ('FUEL', 1)
target = 'FUEL', 1
oreNeeded = calculateCost(target, chemicalDict, outputDict, 0)
needCounterDict = dict()
for reactant in outputDict.keys():
    needCounterDict[reactant] = 0
needCounterDict['ORE'] = 0

print(oreNeeded)
