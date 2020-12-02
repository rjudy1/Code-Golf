# solution to 2019 P1
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


number = readCSV('num.csv')
sum = 0
for n in number:
    sum += calculateFuel(0, n)
print(sum)