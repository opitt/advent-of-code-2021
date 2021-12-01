# https://adventofcode.com/2021/day/1
from rich import print
from more_itertools import windowed   
import os

def solve1(sonars):
    #ret=sum( [s2>s1 for s1,s2 in zip(sonars[:-1],sonars[1:])]  )
    ret=sum(w[1]>w[0] for w in windowed(sonars, 2))
    return ret

def solve2(sonars):
    #sonars_3avg = [sum(sonars[i:i+3]) for i in range(len(sonars)-2)]
    sonars_3avg = [sum(w) for w in windowed(sonars, 3)]
    return solve1(sonars_3avg)

def main():
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    lines = list(map(int, map(str.strip, lines)))

    # PART 1
    result=solve1(lines)
    print(
        f"The depth increases {result} times"
    )
    # The depth increases 1688 times

    # PART 2
    result = solve2(lines)
    print(
        f"The depth increases {result} times"
    )
    # The depth increases 1728 times

main()
