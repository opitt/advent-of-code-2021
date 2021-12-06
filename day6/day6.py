# https://adventofcode.com/2021/day/6
import os
from rich import print
from collections import Counter
from copy import deepcopy


def sim1_day(fishes):
    # Each day, a 0 becomes a 6 and adds a new 8 to the end of the list,
    # while each other number decreases by 1 if it was present at the start of the day.
    new_fish = []
    for i, f in enumerate(fishes):
        if f == 0:
            fishes[i] = 6
            new_fish.append(8)
        else:
            fishes[i] -= 1
    fishes.extend(new_fish)

def solve1(fishes, days):
    # brute force simulation ... BAD
    fish_sim = fishes[:]
    for day in range(days):
        sim1_day(fish_sim)
    return len(fish_sim)

def solve2(fishes, days):
    # Each day, a 0 becomes a 6 and adds a new 8 to the end of the list,
    # while each other number decreases by 1 if it was present at the start of the day.
    fish_sim = [fishes.count(i) for i in range(9)]
    next_gen = [0] * 9
    for _ in range(days):
        next_gen[0] = fish_sim[1]
        next_gen[1] = fish_sim[2]
        next_gen[2] = fish_sim[3]
        next_gen[3] = fish_sim[4]
        next_gen[4] = fish_sim[5]
        next_gen[5] = fish_sim[6]
        next_gen[6] = fish_sim[7]
        next_gen[7] = fish_sim[8]
        if fish_sim[0] > 0:
            next_gen[8] = fish_sim[0]
            next_gen[6] += fish_sim[0]
        else:
            # reset Fish 8  ... since there are no new fishes
            next_gen[8] = 0
        fish_sim = next_gen[:]
    return sum(fish_sim)


def main():
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    # 1,2,4,3,5 =>
    fishes = list(map(int, lines[0].strip().split(",")))

    # PART 1
    result = solve1(fishes, 80)
    print(f"The solution 1 is {result} ")
    # answer: 396210

    # PART 2
    result = solve2(fishes, 256)
    print(f"The solution 2 is {result} ")
    # answer: 1770823541496


main()
