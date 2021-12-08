# https://adventofcode.com/2021/day/8
import os
from rich import print
from collections import Counter, defaultdict


def solve():
    seg_nums = {
        0: "1110111",  # ABCdEFG
        1: "0010010",  # abCdeFg
        2: "1011101",  # AbCDEfG
        3: "1011011",  # AbCDeFG
        4: "0111010",  # aBCDeFg
        5: "1101011",
        6: "1101111",
        7: "1010010",
        8: "1111111",
        9: "1111011",
    }
    pass


def main(part=0):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    #
    sig_patterns = [
        list(map("".join,map(sorted, line.split(" | ")[0].split()))) for line in lines
    ]
    digit_output = [
        list(map("".join,map(sorted, line.split(" | ")[1].split()))) for line in lines
    ]

    # PART 1
    if 1 in part:
        result = sum([sum(map(lambda d:1 if len(d) in (2,4,7,3) else 0,digi)) for digi in digit_output])
        print(f"The solution 1 is {result} ")
        # answer: 318

    # PART 2
    if 2 in part:
        result = None
        print(f"The solution 2 is {result} ")
        # answer:


if __name__ == "__main__":
    main([1])
    # t = timeit.Timer(lambda: main([2]))
    # print(t.timeit(1),"sec")
