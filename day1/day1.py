# https://adventofcode.com/2021/day/1
from rich import print
import os

def main():

    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()

    # HANDLE INPUT
    lines = list(map(str.strip, lines))
    lines = list(map(int, lines))
    # lines = [1941, 1887, 1851, ...]

    # CALCULATE PART 1
    # example:
    e1_2020 = [2020 - expense for expense in lines]
    result = [d for d in e1_2020 if d in lines]
    print(
        f"The entries ({result[0]},{result[1]}) sum up to 2020, and multiplied result in {result[0]*result[1]}"
    )

    pass
    result = None
    print(f"{result} ...")

    # CALCULATE PART 2
    pass
    result = None
    print(f"{result} ...")


main()
