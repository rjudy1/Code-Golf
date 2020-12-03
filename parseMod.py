# Input parsers for code golf
# Author:   Rachael Judy
# Written:  12/1/20
# Modified: 12/3/20

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


# array with each row as element in string form
def readCSV_row(filename, delim='\n', delim2 = ' '):
    array = readCSV_rowEl(filename, delim)
    finished = []
    for el in array:
        for item in el:
            finished.append(item)
    return finished


# array of array of each line, split into elements on line (rowEl)
def readCSV_rowEl(filename, delim=' '):
    num = []
    with open(filename) as file:
        reader = csv.reader(file, delimiter=delim)
        for row in reader:
            temp = []
            for s in row:
                temp.append(s)
            num.append(temp)
    return num


# reads in as one big array
def readCSV_single(filename):
    num = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            for s in row:
                for c in s:
                    num.append(c)

    return num