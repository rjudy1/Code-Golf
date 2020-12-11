# Advent of Code 2019 Day 6
# Author:   Rachael Judy
# Date Mod: 12/2/2020
# Total Orbits


import parseMod

# occupied_count orbits from a single key recursively
def countOrbits(key, num, planets):
    if key != 'COM' and key is not None:
        num += 1
        num = countOrbits(planetDict[key], num, planets)
    return num


# get total number from all planets in dictionary
def getTotalOrbits(planetDict):
    totalOrbits = 0
    for planet in planetDict.keys():
        totalOrbits += countOrbits(planet, 0, planetDict)

    return totalOrbits


# build predecessor list of orbits back to COM, not including self
def buildPredecessorList(key, planets):
    predList = []
    while key != 'COM':
        predList.append(planets[key])
        key = planets[key]
    predList.append('COM')
    return predList


# occupied_count transfer from x to y by traveling to common predecessor
def countTransfers(x, y, planets):
    predX = buildPredecessorList(x, planets)
    predY = buildPredecessorList(y, planets)

    # occupied_count how many transfers x will have to make to get to the common predecessor
    transfersX = 0
    found = False

    # look for common predecessor, counting steps for each to get there
    for i in range(len(predX)):
        transfersX += 1  # how far back has X moved
        transfersY = 0  # set to zero each time check
        for j in range(len(predY)):
            transfersY += 1
            # if match found, store the total steps and get out of loop
            if predX[i] == predY[j]:
                found = True
                transfersX += transfersY
                break
        if found:
            break

    return transfersX


# read from file
orbits = parseMod.readCSV_row('data/6orbits.csv')

# create dictionary of relationships
# key will be planet and value will be predecessor
planetDict = dict()
planetDict['COM'] = None
for relationship in orbits:
    keyValue = relationship.split(')')
    planetDict[keyValue[1]] = keyValue[0]

# get orbits and transfers from you to santa
totalOrbits = getTotalOrbits(planetDict)
transfer = countTransfers(planetDict['YOU'], planetDict['SAN'], planetDict)

# display
print("Total Orbits", totalOrbits)
print("Transfer Distance", transfer)
