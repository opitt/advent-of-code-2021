# https://adventofcode.com/2021/day/7
import os
from rich import print
from collections import Counter, defaultdict
from copy import deepcopy


def solve1(crabs):
    # from_to_fuel={1:{2:2},2:{1:1}}
    from_to_fuel = {}
    p_cnt = Counter(crabs)
    pos = sorted(p_cnt.keys())
    for p_from in pos:
        from_to_fuel[p_from] = {}
        for p_to in pos:
            steps = abs(p_to - p_from)
            from_to_fuel[p_from][p_to] = steps * p_cnt[p_from]
    to_fuelneed = {}
    for p_to in pos:
        # test, if this is the best
        to_fuelneed[p_to] = sum(from_to_fuel[p_from][p_to] for p_from in pos)
    return min(to_fuelneed.values())


def solve2(crabs):
    # from_to_fuel={1:{2:2},2:{1:1}}
    from_to_fuel = {}
    p_cnt = Counter(crabs)
    pos = sorted(p_cnt.keys())
    for p_from in pos:
        from_to_fuel[p_from] = {}
        for p_to in range(min(pos), max(pos) + 1):
            steps = abs(p_to - p_from)
            from_to_fuel[p_from][p_to] = (steps * (steps + 1) // 2) * p_cnt[p_from]
    to_fuelneed = {}
    for p_to in range(min(pos), max(pos) + 1):
        # test, if this is the best
        to_fuelneed[p_to] = sum(from_to_fuel[p_from][p_to] for p_from in pos)
    return min(to_fuelneed.values())


def main():
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    # 1,2,4,3,5 =>
    crabs = list(map(int, lines[0].strip().split(",")))

    # PART 1
    result = solve1(crabs)
    print(f"The solution 1 is {result} ")
    # answer: 323647

    # PART 2
    result = solve2(crabs)
    print(f"The solution 2 is {result} ")
    # answer:


main()
