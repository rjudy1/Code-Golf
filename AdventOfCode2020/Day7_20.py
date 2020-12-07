# Advent of Code 2020 - Day 7

# Author:   Rachael Judy
# Date:     12/7/2020
# Purpose:  Determine how many bags could contain a gold bag and how many bags a gold bag could contain


import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# set phase
phase = 2


# combine array elements that are strings into string, delim separated
def arrayToString(array, delim=' '):
    string = ''
    for x in array:
        string += x + delim
    return string


# count the number of bags that could contain source
def countContainers(source):
    global content_dict, count

    # look for predecessor of source
    for bag in content_dict:
        for container in content_dict[bag]:
            # if bag could contain type and pred path not already searched
            if container[0] == source and bag not in bags_collected:
                # add to collection
#                print(bag)
                bags_collected.append(bag)
                count += 1

                # check what could could contain the bag that contains source
                countContainers(bag)


# count bags that could be contained in <number> <source> bags, recursive
def countContains(source, number):
    global count, content_dict

    # check each possible container inside the source
    for bag in content_dict[source]:
        # if contains nothing, path done
        if bag[0] == 'other bags. ':
            return

        # number of bag inside source, add what it could contain
#        print(bag[0])
        amount = bag[1] * number
        countContains(bag[0], amount)
        count += amount


# get input
rules = parseMod.readCSV_rowEl('data/7bags.csv', ' ')

global content_dict
content_dict = dict()
global count
count = 0
global bags_collected
bags_collected = []

# go through each rule, placing outputs and inputs in content_dict
for rule in rules:
    # contains blank lines
    if rule != '':
        bag_type = arrayToString(rule[0:2])
        content_dict[bag_type] = []

    # populate dictionary with output : [input tuple of type and number]
    for i in range(4, len(rule), 4):
        # special condition for 'no other bags. '
        if rule[i] == 'no':
            rule[i] = 0
        content_dict[bag_type].append((arrayToString(rule[i + 1:i + 3]), int(rule[i])))

# phase 1 - bags that could hold shiny gold
if phase == 1:
    countContainers('shiny gold ')
    print("#Bags that could hold shiny gold:", count)

# phase 2 - bags that shiny gold could hold
else:
    countContains('shiny gold ', 1)
    print("#Bags that shiny gold could hold:", count)

