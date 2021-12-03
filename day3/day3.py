# https://adventofcode.com/2021/day/3
import os
from rich import print


def solve1(rep):
    most_least = [
        ("1", "0") if col.count("1") > col.count("0") else ("0", "1")
        for col in list(zip(*rep))
    ]
    gamma_rate = int("".join(ml[0] for ml in most_least), 2)
    epsilon_rate = int("".join(ml[1] for ml in most_least), 2)
    return gamma_rate * epsilon_rate


def solve2(rep_org):
    def calc(what, rep):
        bit = 0
        while len(rep) > 1:
            # get the bits of all remaining numbers in the report at the current bit position
            bits = [num[bit] for num in rep]
            if what == "oxy":
                # keep 1, if there are less 0s than 1s (otherwise keep 0)
                keep = "1" if bits.count("1") >= bits.count("0") else "0"
            else:
                # keep 1, if there are less 1s than 0s (otherwise keep 0)
                keep = "1" if bits.count("1") < bits.count("0") else "0"
            # keep only numbers that have the keep bit at the position
            rep = [num for num in rep if num[bit] == keep]
            bit += 1
        return int(rep[0], 2)

    oxy_rate = calc("oxy", rep_org[:])
    co2_rate = calc("co2", rep_org[:])
    return oxy_rate * co2_rate


def main():
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    report = list(map(str.strip, lines))

    # PART 1
    result = solve1(report)
    print(f"The solution 1 is {result} ")
    # answer: 3901196

    # PART 2
    result = solve2(report)
    print(f"The solution 2 is {result} ")
    # answer:


main()
