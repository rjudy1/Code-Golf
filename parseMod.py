# Input parsers for code golf
# Author:   Rachael Judy
# Written:  12/1/20
# Modified: 11/20/22

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

cookie = "53616c7465645f5f5bb83a61626d763169fd6291066972ad0a8815efdc0495ad90319c5f17495f97c183f42e69644dd0800b82fab928656da9e4afb9b959a846"


def submit(result, part='a', year=2022, day=1):
    global cookie
    aocd.submit(result, part=part, day=day, year=year, session=cookie)

# create data.csv file with the data for given day
def createDataFile(year, day):
    cookie = "53616c7465645f5f5bb83a61626d763169fd6291066972ad0a8815efdc0495ad90319c5f17495f97c183f42e69644dd0800b82fab928656da9e4afb9b959a846"
    filename = "data/" + str(day).zfill(2) + "data.csv"
    f = open(filename, 'w')
    f.write(aocd.get_data(cookie, day, year))
    f.close()


# to break into array of numbers
def readCSVInts(filename, delim=','):
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
    finished = []
    for el in array:
        for item in el:
            finished.append(item)
    return finished


# array of array of each line, split into elements on line (rowEl)
def readCSV_rowEl(filename, delim=' '):
    rowEl = []
    with open(filename) as file:
        reader = csv.reader(file, delimiter=delim)
        for row in reader:
            temp = []
            for s in row:
                temp.append(s)
            rowEl.append(temp)
    return rowEl


# reads in as one big array of characters
def readCSV_single(filename):
    inp = open(filename).read()
    array = [c for c in inp]
    return array


# array of array of each line, split into elements on line (rowEl)
# NOTE: For whatever reason, doesn't read last bunch so \n random content must be hand added
def readCSV_batch(filename, delim=' ', addsep=''):
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


def to_base(n, base):
    s = ''
    while n:
        s, n = str(n % base) + s, int(n/base)
    return s
