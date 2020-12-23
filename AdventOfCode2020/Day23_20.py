# Advent of Code 2020 - Day 23

# Author:   Rachael Judy
# Date:     12/23/2020
# Purpose:  Play repetitive cup shuffle game that finds the order after 100 shuffles. Then, expand the list to 1M count
#           and 10M turns (takes about 12 seconds anaconda) - set inp for own use - LL class and list too slow

def play(seed, count, shuffles):  # takes initial values, number of cups, number of shuffles
    # cups LL of number relationships in x : y where y is clockwise of x
    cups = {}
    for i in range(1, count):
        if i < len(seed):
            cups[int(seed[i-1])] = int(seed[i])
            last = cups[int(seed[i-1])]
        else:
            cups[last] = i+1
            last = cups[last]
    cups[last] = int(seed[0])

    # set initial source and perform shuffles
    source = int(seed[0])
    for turn in range(shuffles):
        moving = [cups[source], cups[cups[source]], cups[cups[cups[source]]], 0]  # cups to be moved
        cups[source] = cups[cups[cups[cups[source]]]]  # the fourth one is now linked to source

        # find destination
        dest = source - 1
        while dest in moving:  # will repeat at most 4 times
            dest = (dest - 1) if dest > 1 else count

        # place the three after destination but before what destination pointed to
        cups[dest], cups[moving[2]] = moving[0], cups[dest]
        source = cups[source]  # get next source (current cup)

    # part 1 and 2 displays
    if count < 10:  # print list not including one, part 1
        start = 1
        print('part 1: ', end='')
        for i in range(len(cups)-1):
            print(cups[start], end='')
            start = cups[start]
        print()
    else:
        print('part 2: ', end='')
        print(cups[1] * cups[cups[1]])


inp = '327465189'  # set this value to do your own input
play(inp, 9, 100)  # 100 shuffles, 9 cups
play(inp, 1_000_000, 10_000_000)  # 10M shuffles, 1M cups, part 2