# https://adventofcode.com/2021/day/7
import os
from rich import print
from collections import Counter, defaultdict
from copy import deepcopy


def solve(crabs, more_fuel):
    p_cnt = Counter(crabs)
    crab_pos = p_cnt.keys()
    all_pos = range(min(crab_pos), max(crab_pos) + 1)
    from_to_fuel = {}  # from_to_fuel={1:{2:2},2:{1:1}}
    for p_from in crab_pos:
        from_to_fuel[p_from] = {}
        for p_to in all_pos:
            steps = abs(p_to - p_from)
            if more_fuel:
                fuel = steps * (steps + 1) // 2 * p_cnt[p_from]
            else:
                fuel = steps * p_cnt[p_from]
            from_to_fuel[p_from][p_to] = fuel
    to_fuelneed = {
        p_to: sum(from_to_fuel[p_from][p_to] for p_from in crab_pos) for p_to in all_pos
    }
    return min(to_fuelneed.values())


def main():
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    # 1,2,4,3,5 =>
    crabs = list(map(int, lines[0].strip().split(",")))

    # PART 1
    result = solve(crabs, False)
    print(f"The solution 1 is {result} ")
    # answer: 323647

    # PART 2
    result = solve(crabs, True)
    print(f"The solution 2 is {result} ")
    # answer: 87640209


main()
