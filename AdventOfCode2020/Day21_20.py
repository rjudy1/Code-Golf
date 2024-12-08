# Advent of Code 2020 - Day 21

# Author:   Rachael Judy
# Date:     12/21/2020
# Purpose:  Sort through the ingredients list for ones that are allergen free and then compile the alphabetical
#           by allergen list of ingredients

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import parseMod


ingredients_list = parseMod.readCSV_row('data/21ingredients.csv', '\n')

# parse input to allergens dictionary
allergen_dict = {}  # will have allergen : list of list of ingredients
for food in ingredients_list:
    allergens = food[food.ind("(") + len("contains "):-1].split()
    ingredients = food[:food.ind("(")].split()
    for a in range(len(allergens)):  # strip off the spare commas in allergen list
        allergens[a] = allergens[a].strip(",")

    for alle in allergens:  # create dictionary entry for allergen
        if alle not in allergen_dict:
            allergen_dict[alle] = [ingredients]
        else:
            allergen_dict[alle].append(ingredients)

all_set = set()  # for all ingredients
# finds unsafe set for each allergen
for allergen in allergen_dict:
    unsafe_set = set(allergen_dict[allergen][0])
    for ingr_list in allergen_dict[allergen]:  # get the ingredients that could contain the allergen
        unsafe_set = set(unsafe_set.intersection(ingr_list))
        all_set = set(all_set.union(set(ingr_list)))
    allergen_dict[allergen] = unsafe_set

# find safe set of all foods by removing unsafe from the list of all
for allergy_set in allergen_dict.values():
    all_set = set(all_set - allergy_set)

# sea_monster_count the appearances of useful ingredients
count = 0
for line in ingredients_list:
    for ingr in all_set:
        count += 1 if (ingr + " ") in line else 0  # watch out for the overlap in naming strings by adding a space
print("Part 1: ", count)

final_dict = {}
for i in allergen_dict:  # go back to list because duplicates are gone now
    allergen_dict[i] = list(allergen_dict[i])
for i in range(len(allergen_dict)):  # find the appearance of the only possible ingredient, remove, repeat
    for allergen in allergen_dict:
        if len(allergen_dict[allergen]) == 1:
            value = allergen_dict[allergen][0]
            final_dict[allergen] = value
            for alle in allergen_dict:  # remove the ingredient from possibilities
                if value in allergen_dict[alle]:
                    allergen_dict[alle].remove(value)

print("Part 2 (omit last comma): ", end='')
for key in sorted(final_dict.keys()):  # print alphabetical by key, comma seperated
    print(final_dict[key], end=',')
