# https://adventofcode.com/2021/day/9
import os
from rich import print
from math import prod

MAXY = 0    # max vertical index (length of map-1)
MAXX = 0    # max horizonal index (width of map-1)
DIRECTIONS = ((0,-1),(0,1),(-1,0),(1,0)) # diff to current position to find adjacent positions


def is_low(height_map, current_y, current_x):
    height_current = height_map[current_y][current_x]
    for dir_y, dir_x in DIRECTIONS:
        next_y=current_y+dir_y
        next_x=current_x+dir_x
        if 0<=next_y<=MAXY and 0<=next_x<=MAXX:
            height_next = height_map[next_y][next_x]
            if height_current >= height_next:return False
    return True


def solve(height_map):
    lows = []
    for y in range(MAXY+1):
        for x in range(MAXX+1):
            if is_low(height_map, y, x):lows.append(height_map[y][x])
    return sum(lows) + len(lows)


def explore_up(height_map_marked, height_current, current_y, current_x):
    height_map_marked[current_y][current_x] = -1 # mark as visited and counted
    basin_size = 0
    for dir_y, dir_x in DIRECTIONS: #up, lef, right, down
        next_y=current_y+dir_y
        next_x=current_x+dir_x
        if 0<=next_y<=MAXY and 0<=next_x<=MAXX:
            height_next = height_map_marked[next_y][next_x]
            if height_next not in (9,-1): 
                basin_size += 1+ explore_up(height_map_marked, height_next, next_y, next_x)
    return basin_size


def solve2(height_map):
    basin_sizes = []
    for y in range(MAXY+1):
        for x in range(MAXX+1):
            height = height_map[y][x]
            if height not in (9,-1) and is_low(height_map, y, x):
                basin_size = 1 + explore_up(height_map, height, y, x)
                basin_sizes.append(basin_size)
    # multiply the 3 biggest basin sizes
    res = prod(sorted(basin_sizes, reverse=True)[:3])
    return res

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
