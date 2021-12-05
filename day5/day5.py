# https://adventofcode.com/2021/day/5
import os
from rich import print
import math


def mark_horiverti_line(vent_map, x1, y1, x2, y2):
    if not (x1 == x2 or y1 == y2):
        return
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            vent_map[y][x] += 1


def solve1(lines_xy, x_max, y_max):
    vent_map = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]
    for x1, y1, x2, y2 in lines_xy:
        mark_horiverti_line(vent_map, x1, y1, x2, y2)
    overlaps = sum([1 for line in vent_map for cell in line if cell > 1])
    return overlaps


def mark_diaghoriverti_line(vent_map, x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        mark_horiverti_line(vent_map, x1, y1, x2, y2)
        return
    sign=lambda n: 1 if n>=0 else -1
    xsign = sign(x2 - x1)
    ysign = sign(y2 - y1)
    for d in range(abs(x1 - x2) + 1):
        vent_map[y1 + (d * ysign)][x1 + (d * xsign)] += 1


def solve2(lines_xy, x_max, y_max):
    vent_map = [[0 for _ in range(x_max + 1)] for _ in range(y_max + 1)]
    for x1, y1, x2, y2 in lines_xy:
        mark_diaghoriverti_line(vent_map, x1, y1, x2, y2)
    overlaps = sum([1 for line in vent_map for cell in line if cell > 1])
    return overlaps


def main():
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    # 0,9 -> 5,9 => [0,9,5,9]
    lines = [list(map(int, l.replace(" -> ", ",").strip().split(","))) for l in lines]
    x_max = max([max(line[0], line[2]) for line in lines])
    y_max = max([max(line[1], line[3]) for line in lines])

    # PART 1
    result = solve1(lines, x_max, y_max)
    print(f"The solution 1 is {result} ")
    # answer: 8111

    # PART 2
    result = solve2(lines, x_max, y_max)
    print(f"The solution 2 is {result} ")
    # answer: 22088


main()
