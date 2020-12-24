# Advent of Code 2018 - Day 8

# Author:   Rachael Judy
# Date:     12/23/2020
# Purpose:  Read tree in (space separated numbers) with child and metadata attributes and find metadata sum and node val

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod
inp = parseMod.readCSV('data/8tree.csv', ' ')

global ptr
ptr = 0  # pointer for collecting the data
nodes = []  # list of Node objects


class Node:  # has children
    def __init__(self, id_p):
        self.id = id_p  # pointer found at
        self.children = []  # children Node objects
        self.metadata = []  # numbers

    def sum_metadata(self):  # sum all it and its children's metadata (recursive)
        return sum(m for m in self.metadata) + sum(c.sum_metadata() for c in self.children)

    def calculate_node_val(self):  # return sum of own data if no children, otherwise return sum of children's values
        return sum(m for m in self.metadata) if len(self.children) == 0 \
            else sum(self.children[x-1].calculate_node_val() for x in self.metadata if 0 < x <= len(self.children))


def read_node():  # creates a nested node
    global ptr

    node = Node(ptr)  # create node
    child_count = inp[ptr]
    metadata_count = inp[ptr + 1]
    ptr += 2

    # read node children
    node.children = [read_node() for i in range(child_count)]

    # read metadata
    node.metadata = [inp[ptr+i] for i in range(metadata_count)]
    ptr += len(node.metadata)

    return node


data = read_node()
print("part 1: ", data.sum_metadata())
print("part 2: ", data.calculate_node_val())
