# https://adventofcode.com/2021/day/7
import os
from rich import print
from collections import Counter, defaultdict
import timeit


def solve(crabs, more_fuel):
    p_cnt = Counter(crabs)
    crab_pos = p_cnt.keys()
    all_pos = range(min(crab_pos), max(crab_pos) + 1)
    min_fuel=None
    for p_to in all_pos:
        cur_fuel=0
        for p_from in crab_pos:
            steps = abs(p_to - p_from)
            if more_fuel:
                fuel = steps * (steps + 1) // 2 * p_cnt[p_from]
            else:
                fuel = steps * p_cnt[p_from]
            cur_fuel+=fuel
        min_fuel = cur_fuel if min_fuel==None or min_fuel>cur_fuel else min_fuel

    return min_fuel


def main(part=0):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    # 1,2,4,3,5 =>
    crabs = list(map(int, lines[0].strip().split(",")))

    # PART 1
    if 1 in part:
        result = solve(crabs, False)
        print(f"The solution 1 is {result} ")
        # answer: 323647

    # PART 2
    if 2 in part:
        result = solve(crabs, True)
        print(f"The solution 2 is {result} ")
        # answer: 87640209

if __name__ == "__main__":
    main([1,2])
    #t = timeit.Timer(lambda: main([2]))
    #print(t.timeit(1),"sec")
