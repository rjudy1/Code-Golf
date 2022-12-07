# Advent of Code 2022 Day 7
# Author:   Rachael Judy
# Date:     12/7/22
# Purpose:  Determine file system from cd and ls commands (build tree - slightly clumsy),
#           sum sizes of directories less than 1000000,
#           determine the smallest file needed to delete for update

import parseMod

stage = 'b'
day = 7
year = 2022
parseMod.createDataFile(year=2022, day=7)
commands = parseMod.readCSV_row("data/" + str(day).zfill(2) + "data.csv")
commands.append('$ cd /')  # add this to always go back up the top file at end
index = 0


class File:
    def __init__(self, name='/', parent=None, size=0):
        self.name = name
        self.parent = parent
        self.size = size
        self.children = {}  # names to children trees


# construct tree from commands
def construct_tree(commands, file=None):
    def update_sizes(tree):
        for child in tree.children:
            tree.size += update_sizes(tree.children[child]).size
        return tree

    def build_from_commands(commands, file=None):
        global index
        while index < len(commands):
            c = commands[index].split(' ')
            if c[1] == 'ls':
                pass
            elif c[1] == 'cd':
                if c[2] == '/':
                    if file is None:
                        file = File('/', None, True)
                    else:
                        while file.parent is not None:
                            file = file.parent
                elif c[2] == '..':
                    # go back up the tree (return current state ig)
                    if file.parent is not None:
                        return file.parent
                else:
                    file.children[c[2]] = File(c[2], file)
                    index += 1
                    file = build_from_commands(commands, file.children[c[2]])
            else:
                file.children[c[1]] = File(c[1], file, int(c[0]) if c[0] != 'dir' else 0)

            index += 1
        return file

    return update_sizes(build_from_commands(commands))


# determine sum of all folder sizes under maximum size
def solve_a(tree, maximum_size):
    tree_size = tree.size if tree.size < maximum_size and len(tree.children) else 0
    return tree_size + sum(solve_a(tree.children[child], maximum_size) for child in tree.children)


# determine folder of minimum size needed
def solve_b(tree, minimum_size):
    remove_size = tree.size if tree.size > minimum_size and len(tree.children) else 1000000000
    for child in tree.children:
        remove_size = min(remove_size, solve_b(tree.children[child], minimum_size))
    return remove_size


# construct tree
tree = construct_tree(commands)

if stage == 'a':
    result = solve_a(tree, 100000)
else:
    result = solve_b(tree, tree.size - 40000000)

print("SUBMITTING RESULT: ", result)
parseMod.submit(result, part=stage, day=day, year=year)
