# Advent of Code 2023 Day 12
# Author:   Rachael Judy
# Date:     12/12/23
# Purpose:  nonograms with incomplete patterns, try possible placements of groups and count working versions

from functools import cache
import parseMod

ready = True  # 6949, 51456609952403
day = 12
stage = 'b'
year = 2023

parseMod.createDataFile(year=year, day=day)
map = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv", delim=' ')


@cache  # cache the result for each placement
def place(groups: tuple, template: str):  # recursively worst case O(len(template)^len(groups))
    def placement_valid(position: int, size: int, template: str):  # O(position+size)
        return not (position + size > len(template)
                    or position + size < len(template) and template[position + size] == '#'
                    or '.' in template[position:position + size])
    perms = 0
    for i in range(0, len(template) - sum(groups) + 1 - len(groups) + 1):
        if placement_valid(i, groups[0], template):  # can this group start at this location
            if len(groups) != 1:  # not finished with groups, keep recursing
                perms += place(groups[1:], template[i+groups[0]+1:])
            elif i+groups[0] == len(template) or template[i+groups[0]:].count('#') == 0:  # working result
                perms += 1
        if template[i] == '#':  # forced to try to place here so can't continue looking for new spots for group
            break
    return perms


result = 0
for template, groupings in map:
    if stage == 'b':  # stage b makes each multiply by 5
        template = '?'.join(template for _ in range(5))
        groupings = ','.join(groupings for _ in range(5))
    groupings = tuple(int(s) for s in groupings.split(','))
    place.cache_clear()  # clear cache so subproblems don't screw each other up
    result += place(groupings, template)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
