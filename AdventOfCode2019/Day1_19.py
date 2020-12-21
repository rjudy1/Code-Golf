# Advent of Code 2019 - Day 1

# Author:   Rachael Judy
# Date:     12/1/20
# Purpose:  Calculate fuel needed, part 1, remove recursion
import csv

def readCSV(filename):
    num = []
    with open(filename) as file:
        reader = csv.reader(file, delimiter='\n')
        for row in reader:
            for s in row:
                num.append(int(s))
    return num


def calculateFuel(fuel, mass):
    if mass <= 0:
        return fuel
    else:
        addFuel = int(mass / 3) - 2
        if addFuel > 0:
            fuel += addFuel
        fuel = calculateFuel(fuel, addFuel)
        return fuel


number = readCSV('data/1num.csv')
sum = 0
for n in number:
    sum += calculateFuel(0, n)
print(sum)