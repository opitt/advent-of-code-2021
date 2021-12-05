# https://adventofcode.com/2021/day/5
import os
from rich import print

def mark_horiverti_line(vent_map, x1, y1, x2, y2):
    if not (x1 == x2 or y1 == y2):
        return
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            vent_map[y][x] += 1

def mark_diaghoriverti_line(vent_map, x1, y1, x2, y2):
    if x1 == x2 or y1 == y2:
        return mark_horiverti_line(vent_map, x1, y1, x2, y2)
    sign=lambda n: 1 if n>=0 else -1
    xsign, ysign = sign(x2 - x1), sign(y2 - y1)
    # only 45 degrees given, i.e. x and y change by the same value
    for d in range(abs(x1 - x2) + 1):
        vent_map[y1 + ysign * d][x1 + xsign * d] += 1

def calc_overlaps(vent_map):
    return sum(1 for line in vent_map for cell in line if cell > 1)

def solve1(lines_xy, vent_map):
    for x1, y1, x2, y2 in lines_xy:
        mark_horiverti_line(vent_map, x1, y1, x2, y2)
    return calc_overlaps(vent_map)

def solve2(lines_xy, vent_map):
    for x1, y1, x2, y2 in lines_xy:
        mark_diaghoriverti_line(vent_map, x1, y1, x2, y2)
    return calc_overlaps(vent_map)

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
    vent_map = [[0] * (x_max + 1) for _ in range(y_max + 1)]
    result = solve1(lines, vent_map)
    print(f"The solution 1 is {result} ")
    # answer: 8111

    # PART 2
    vent_map = [[0] * (x_max + 1) for _ in range(y_max + 1)]
    result = solve2(lines, vent_map)
    print(f"The solution 2 is {result} ")
    # answer: 22088


main()
