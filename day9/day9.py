# https://adventofcode.com/2021/day/9
import os
from rich import print
from math import prod
from copy import deepcopy


def is_low(H, y, x):
    height = H[y][x]
    for dy, dx in DIRECTIONS:
        if 0<=y+dy<=MAXY and 0<=x+dx<=MAXX:
            height_neighbour = H[y+dy][x+dx]
            if height >= height_neighbour:
                return False
    return True


def solve(H):
    lows = []
    for y in range(len(H)):
        for x in range(len(H[0])):
            if is_low(H, y, x):
                lows.append(H[y][x])
    return sum(lows) + len(lows)


def explore_up(H, height, y, x):
    H[y][x] = -1
    explored_basins = 0
    for dy, dx in DIRECTIONS:
        ny=y+dy
        nx=x+dx
        if 0<=ny<=MAXY and 0<=nx<=MAXX:
            height_neighbour = H[ny][nx]
            if height_neighbour not in (9,-1): 
                # if height_neighbour != 9 and height_neighbour > height:
                explored_basins += 1+ explore_up(H, height_neighbour, ny, nx)
    return explored_basins


def solve2(height_map):
    basins = []
    for y in range(len(height_map)):
        for x in range(len(height_map[0])):
            if is_low(height_map, y, x):
                height = height_map[y][x]
                basin_size = 1 + explore_up(deepcopy(height_map), height, y, x)
                # basin_size = 1 + explore_up(height_map, height, y, x)
                basins.append(basin_size)
    res = prod(sorted(basins, reverse=True)[:3])
    return res


MAXY = 0
MAXX = 0
DIRECTIONS = ((0,-1),(0,1),(-1,0),(1,0))

def main(input_name):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    heights = [list(map(int, line.strip())) for line in lines]

    global MAXX, MAXY
    MAXY = len(heights) - 1
    MAXX = len(heights[0]) - 1

    result = solve(heights)
    print(f"The solution 1 is {result} ")
    # answer: 444

    result = solve2(heights)
    print(f"The solution 2 is {result} ")
    # answer: 1168440

if __name__ == "__main__":
    main("input.txt")
