# Advent of Code 2020 - Day 4

# Author:   Rachael Judy
# Date:     12/4/2020
# Purpose:  Validate passports with different fields/conditions
#               Phase 1: has required fields
#               Phase 2: check that fields meet conditions

import csv
import re
import fileinput
import sys


# set phase
phase = 1
ifile = 'data/4passports.csv'


# array of array of each line, split into elements on line (rowEl)
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
    return batches


# confirm password validity
def checkValidity(details, part=1):
    details = details.split(' ')  # split to each element
    keys = []
    values = []

    # make dictionary of each attribute
    detailsDict = dict()
    for d in details:
        if len(d) != 0:
            d = d.split(':')
            detailsDict[d[0]] = d[1]

    # check all required fields exist
    reqFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid = True
    for field in reqFields:
        if field not in detailsDict.keys():
            valid = False

    # if part 1, done checking, if part 2 continue
    if part == 1:
        return valid
    if part == 2 and valid:
        # check byr, iyr, eyr are 4 digits and in correct range
        if len(detailsDict['byr']) != 4 or \
            int(detailsDict['byr']) > 2002 or int(detailsDict['byr']) < 1920\
            or len(detailsDict['iyr']) != 4 or \
            int(detailsDict['iyr']) < 2010 or int(detailsDict['iyr']) > 2020\
            or len(detailsDict['eyr']) != 4 or \
            int(detailsDict['eyr']) < 2020 or int(detailsDict['eyr']) > 2030:
            valid = False

        # confirm height has units and is in range
        hgt = detailsDict['hgt'][:-2]
        unit = detailsDict['hgt'][-2:]
        if unit == 'cm':
            if int(hgt) < 150 or int(hgt) > 193:
                valid = False
        elif unit == 'in':
            if int(hgt) < 59 or int(hgt) > 76:
                valid = False
        else:
            valid = False

        # make sure hair color only has valid rgb and starts with #
        hcl = detailsDict['hcl']
        _rgbstring = re.compile(r'#[a-fA-F0-9]{6}$')
        if not _rgbstring.match(hcl):
            valid = False

        # check eye color in allowable entries
        ecl = detailsDict['ecl']
        if ecl not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            valid = False

        # confirm 9 digit number
        _rgbstring = re.compile(r'[0-9]{9}$')
        if not _rgbstring.match(detailsDict['pid']):
            valid = False

        return valid


passports = readCSV_batch(ifile)
count = 0
for passport in passports:
    if checkValidity(passport, phase):
        count += 1

print("Valid Passports: ", count)
