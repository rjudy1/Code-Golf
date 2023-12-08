# Advent of Code 2023 Day 7
# Author:   Rachael Judy
# Date:     12/7/23
# Purpose:  poker ordering of hands with five of a kind down to high card, twist of wildcard joker

from collections import Counter
from functools import cmp_to_key
import parseMod

ready = True
day = 7
stage = 'b'
year = 2023

parseMod.createDataFile(year=year, day=day)
array = parseMod.readCSV_rowEl("data/" + str(day).zfill(2) + "data.csv")


def compare(hand1: str, hand2: str):
    def classify(hand: list):
        if stage == 'b':  # convert wildcard to optimal for stage b
            for i, card in enumerate(hand):  # O(5)
                if card == 'J' and hand != list('JJJJJ'):
                    if Counter(hand).most_common(1)[0][0] == 'J':  # O(5), could store Counter instead of redoing
                        hand[i] = Counter(hand).most_common(2)[1][0]  # O(5log2)
                    else:
                        hand[i] = Counter(hand).most_common(1)[0][0]

        hand.sort()  # O(5log5)
        if len(set(hand)) == 1: return 6  # five of a kind
        elif max(hand.count(hand[0]), hand.count(hand[-1])) == 4: return 5  # four of a kind
        elif max(hand.count(hand[0]), hand.count(hand[-1])) == 3 and min(hand.count(hand[0]), hand.count(hand[-1])) == 2:
            return 4  # full house (three and two)
        elif max(hand.count(hand[0]), hand.count(hand[2]), hand.count(4)) == 3: return 3  # three of a kind
        elif len(set(hand)) == 3: return 2  # two pair
        elif len(set(hand)) == 4: return 1  # one pair
        return 0  # all unique

    if classify(sorted(hand1)) < classify(sorted(hand2)):
        return -1
    elif classify(sorted(hand1)) > classify(sorted(hand2)):
        return 1
    else:
        order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        if stage == 'b':  # stage b makes J the lowst
            order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
        for card1, card2 in zip(hand1, hand2):  # O(5)
            if order.index(card1) > order.index(card2):  # O(5)
                return 1
            elif order.index(card1) < order.index(card2):
                return -1
        return 0


ranks = sorted([key for (key, _) in array], key=cmp_to_key(compare))  # O(n log n)
result = sum((ranks.index(hand)+1) * int(bid) for (hand, bid) in array)  # O(n^2), build hand_to_bid dict to make O(n)

if not ready:
    print(f'result: \n{result}')
elif ready:
    print("SUBMITTING RESULT: ", result)
    parseMod.submit(result, part=stage, day=day, year=year)
