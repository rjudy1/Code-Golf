# Advent of Code 2020 - Day 16

# Author:   Rachael Judy
# Date:     12/16/2020
# Purpose:  Parse the list of conditions, my ticket, and other tickets to determine the sum of the invalid numbers on
#           the tickets (part 1). Remove invalid tickets and use what's left to determine what field each number is.
#           Find the product of departure fields on my ticket (part 2)

import copy
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod

# read input
tickets = parseMod.readCSV_rowEl('data/16tickets.csv')

# get the conditions by reading to empty line
condition_list = []
for condition_i, ticket in enumerate(tickets):
    if not len(ticket):
        break

    # store bounds of condition as int
    bounds = [ticket[-3].split('-'), ticket[-1].split('-')]
    for x, c in enumerate(bounds):
        for i, n in enumerate(c):
            bounds[x][i] = int(n)

    # determine name
    if len(ticket) > 4:
        name = ticket[-5] + ' ' + ticket[-4]
    else:
        name = ticket[-4]

    # add the condition to the list
    condition_list.append((name, bounds[0], bounds[1]))  # tuple containing name, bounds

# get list of numbers on my ticket
myTicket = [int(x) for x in tickets[condition_i+2][0].split(',')]
condition_i += 5  # gets to the other tickets

# store the values of the other tickets
other_tickets = []
for i in range(condition_i, len(tickets)):
    temp_ticket = [int(x) for x in tickets[i][0].split(',')]
    other_tickets.append(temp_ticket)

# go through other tickets counting the invalid ones, removing from a copy
new_other_tickets = copy.deepcopy(other_tickets)  # for part 2
error_value = 0
for t in other_tickets:
    for number in t:
        valid = False
        # if invalid number on ticket (meeting none of the conditions), throw out the ticket and add error_value
        for condition in condition_list:
            if condition[1][0] <= number <= condition[1][1] or condition[2][0] <= number <= condition[2][1]:
                valid = True
        if not valid:
            error_value += number
            new_other_tickets.remove(t)  # for part 2

print("Part 1: ", error_value)


# part 2
# store possibilites of matching column for each column
possibilities = []
for num in range(len(new_other_tickets[0])):  # column num = 0, 1, 2, ... - eliminate column wise
    poss_temp = []
    # if column meets condition, save possibility
    for condition in condition_list:
        is_condition = True
        for t in new_other_tickets:  # if one item in column fails, try next condition
            if not (condition[1][0] <= t[num] <= condition[1][1] or condition[2][0] <= t[num] <= condition[2][1]):
                is_condition = False
                break
        if is_condition:
            poss_temp.append(condition[0])

    possibilities.append(poss_temp)

# find the correct ordering by taking the only option available for column name
ordering = ['' for i in range(len(condition_list))]
for _ in range(len(condition_list)):  # repeat until all conditions are saved
    for index, option in enumerate(possibilities):
        if len(option) == 1:
            x = option[0]  # save value
            ordering[index] = x
            for opt in possibilities:
                try:
                    opt.remove(x)  # remove from other options
                except Exception:
                    pass  # in case x not in opt
            break

# compute product of all values on myTicket that have departure
product = 1
for i, title in enumerate(ordering):
    if title.startswith('departure'):
        product *= myTicket[i]

print("Part 2: ", product)
