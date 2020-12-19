# Advent of Code 2020 - Day 19

# Author:   Rachael Judy
# Date:     12/19/2020
# Purpose:  Find messages that match rules - non-recursive p1 and recursive p2

import os
import sys
import re

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


# builds regex recursively for input rule
def build_re(r_num):
    rule = rules_dict[r_num]
    if rule == 'a' or rule == 'b':  # if it needs to match the character, place in string
        return rule
    if len(rule) == 1:  # if only one option, just add the rules content
        return "".join(map(build_re, rule[0]))
    else:  # if multiple paths to follow, add every option to the regex - no memory needed
        return "(?:" + "|".join("".join(map(build_re, r)) for r in rule) + ")"


# get input
input_lines = parseMod.readCSV_row('data/19rules.csv', '\n')

# set rules with each rule having either list of alternatives of rules or character to match
rules_dict = dict()
for i, rule in enumerate(input_lines):
    if len(rule) > 20: break
    rule_break = rule.split()

    recursive_rules, temp = [], []
    for char in rule_break[1:]:
        if char.isnumeric():  # append the rule number
            temp.append(int(char))
        elif char == '|':  # start a new list
            recursive_rules.append(temp)
            temp = []
        else:  # letter in quotes found
            temp.append(char[1])

    recursive_rules.append(temp)  # catch last temp
    rules_dict[int(rule_break[0].strip(':'))] = recursive_rules \
        if recursive_rules[0][0] != 'a' and recursive_rules[0][0] != 'b' else recursive_rules[0][0]

messages = input_lines[i:]

# part 1
the_regex = re.compile("^" + build_re(0) + "$")  # must match the entire string for rule 0 - non-recursive
print("Part 1: ", sum(map(bool, map(the_regex.match, messages))))  # checks match on every message and counts if match

# part 2 - new recursive rules
rules_dict[8] = [[42], [42, 8]]
rules_dict[11] = [[42, 31], [42, 11, 31]]

# at least one rule 42 (line 61, followed by infinitely possible nested 42...31 - rep 5 should be sufficient (line 62)
the_regex_2 = re.compile(f"^(?:{build_re(42)})+?(" + \
                         "|".join(f"(?:{build_re(42)}){{{n}}}(?:{build_re(31)}){{{n}}}" for n in range(1, 5)) + ")$")
print("Part 2: ", sum(map(bool, map(the_regex_2.match, messages))))  # count the number of matches
