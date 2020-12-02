# Input parsers for code golf
# Author:   Rachael Judy
# Written:  12/1/20
# Modified: 12/2/20

import csv

# to break into array of numbers
def readCSV(filename, delim=','):
    num = []
    with open(filename) as file:
        reader = csv.reader(file, delimiter=delim)
        for row in reader:
            for s in row:
                num.append(int(s))
    return num


# to break into an array for each line and each item split by delimiter
def readCSVstr(filename, delim=' '):
    num = []
    with open(filename) as file:
        reader = csv.reader(file, delimiter=delim)
        for row in reader:
            temp = []
            for s in row:
                temp.append(s)
            num.append(temp)
    return num

