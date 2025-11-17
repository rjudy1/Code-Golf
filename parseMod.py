# Input parsers for code golf
# Author:   Rachael Judy
# Written:  12/1/20
# TODO: fix this file eventually as the reading is kind of sloppy/inefficient/not-pythonic, also don't really need to create the file and then read from it every time
# maybe for 2025 aoc I'll just use the library aocd as intended

"""
Usage:
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # to fix placement in folders
import parseMod
x = parseMod.readCSV...
"""


import aocd
import csv
import fileinput
import sys

cookie = "53616c7465645f5fdddf3faeb0ffae0151d986703ba15bbbee335172a12424b99eea671c06fcd0a3bd4d52dc48a8a9b4341130ddac5b7e74860eab128bc20c4d"  # also should read this from environ technically


def submit(result, part='a', year=2022, day=1):
    global cookie
    aocd.submit(result, part=part, day=day, year=year, session=cookie)

# create data.csv file with the data for given day
def createDataFile(year, day) -> None:  # don't actually need to pull the data file, could just get data
    filename = "data/" + str(day).zfill(2) + "data.csv"
    f = open(filename, 'w')
    f.write(aocd.get_data(cookie, day, year))
    f.close()
    return filename


# to break into array of numbers
def readCSVInts(filename, delim=',') -> [int]:
    num = []
    with open(filename) as file:
        reader = csv.reader(file, delimiter=delim)
        for row in reader:
            for s in row:
                num.append(int(s))
    return num


# array with each row as element in string form
def readCSV_row(filename, delim='\n'):
    array = readCSV_rowEl(filename, delim)
    return [item for el in array for item in el]

# array of array of each line, split into elements on line (rowEl)
def readCSV_rowEl(filename, delim=' '):
    with open(filename) as file:
        return [[s for s in row] for row in csv.reader(file, delimiter=delim)]


# reads in as one big array of characters
def readCSV_single(filename):
    inp = open(filename).read()
    array = [c for c in inp]
    return array


############# Any below were specific to a certain day and I'll refactor processing eventually ############
# array of array of each line, split into elements on line (rowEl)
# NOTE: For whatever reason, doesn't read last bunch so \n random content must be hand added
def readCSV_batch(filename):
    # add space to end of every line for formatting use with parsing function
    for line in fileinput.input(filename, inplace=True):
        sys.stdout.write("{} \n".format(line.rstrip()))

    batches = []
    string = ''
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:  # each row of the passport
            if row[0] != ' ':  # passports are separated by blank line with single space
                for r in row:
                    string += r
            else:
                batches.append(string)
                string = ''
        batches.append(string)  # catch the last batch

    return batches


def readCSV_chunk(filename):  # spaced by newline between each section
    # add space to end of every line for formatting use with parsing function
    for line in fileinput.input(filename, inplace=True):
        sys.stdout.write("{} \n".format(line.rstrip()))

    batches = []
    array = readCSV_row(filename)
    last_split = 0
    for idx, row in enumerate(array):
        if row.strip() == '':
            batches.append([val.strip() for val in array[last_split:idx]])
            last_split = idx + 1
    batches.append([val.strip() for val in array[last_split:]])
    return batches
