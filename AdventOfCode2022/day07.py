# Advent of Code 2022 Day 7
# Author:   Rachael Judy
# Date:     12/7/22
# Purpose:  Determine file system from cd and ls commands (build tree),
#           sum sizes of directories less than 1000000,
#           determine the smallest file needed to delete for update

import parseMod

stage = 'a'
day = 7
year = 2022

parseMod.createDataFile(year=year, day=day)
commands = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")
index = 0


class File:
    def __init__(self, name='', parent=None, is_dir=False, size=0):
        self.name = name
        self.parent = parent
        self.is_dir = is_dir
        self.size = size
        self.children = {}  # names to children trees

    def add_child(self, new_tree):
        self.children[new_tree.name] = new_tree


def construct_tree(commands, file):
    global index
    while index < len(commands):
        c = commands[index].split(' ')
        if c[1] == 'ls':
            index += 1

            while index < len(commands) and commands[index].split(' ')[0] != '$':
                c = commands[index].split(' ')
                if c[0] == 'dir':
                    file.add_child(File(c[1], file, True, 0))
                else:
                    file.add_child(File(c[1], file, False, int(c[0])))
                index += 1

        elif c[1] == 'cd':
            if c[2] == '/':
                # only appears at top so going to cheat a little bit
                file = File('/', None, True)
            elif c[2] == '..':
                # go back up the tree (return current state ig)
                if file.parent is not None:
                    return file.parent
            else:
                file.add_child(File(c[2], file, True, 0))
                index += 1
                file = construct_tree(commands, file.children[c[2]])
            index += 1

    while file.parent is not None:
        file = file.parent
    return file


def dfs_sum(tree):
    for child in tree.children:
        tree.size += dfs_sum(tree.children[child])[1]
    return tree, tree.size


def solve_a(tree, maximum_size):
    tree_size = tree.size if tree.size < maximum_size and tree.is_dir else 0
    return tree_size + sum(solve_a(tree.children[child], maximum_size) for child in tree.children)


def solve_b(tree, minimum_size):
    min_size = tree.size if tree.size > minimum_size and tree.is_dir else 1000000000
    for child in tree.children:
        min_size = min(min_size, solve_b(tree.children[child], minimum_size))
    return min_size

# construct tree
tree = construct_tree(commands, None)
tree, size = dfs_sum(tree)

if stage == 'a':
    result = solve_a(tree, 100000)
else:
    result = solve_b(tree, min(30000000, 30000000 - 70000000 + tree.size))

print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
