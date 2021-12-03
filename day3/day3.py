# https://adventofcode.com/2021/day/3
import os
from rich import print

def solve1(rep):
    rep_cols = list(zip(*rep))
    gamma_rate = int(
        "".join("1" if col.count("1") > col.count("0") else "0" for col in rep_cols), 2
    )
    epsilon_rate = int(
        "".join("1" if col.count("1") < col.count("0") else "0" for col in rep_cols), 2
    )
    return gamma_rate * epsilon_rate


def solve2(rep_org):
    bit = 0
    # most_common = ["1" if col.count("1") >= col.count("0") else "0" for col in rep_cols]
    rep=rep_org[:]
    while len(rep)>1:
        bits = [num[bit] for num in rep] 
        keep="1" if bits.count("1") >= bits.count("0") else "0"
        rep = [r for r in rep if r[bit] == keep]
        bit += 1
    oxy_rate = int(rep[0], 2)

    bit = 0
    rep=rep_org[:]
    while len(rep)>1:
        bits = [num[bit] for num in rep] 
        keep="1" if bits.count("1") < bits.count("0") else "0"
        rep = [r for r in rep if r[bit] == keep]
        bit += 1
    co2_rate = int(rep[0], 2)
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
