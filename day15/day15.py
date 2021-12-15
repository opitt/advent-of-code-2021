# https://adventofcode.com/2021/day/14
import os
from rich import print
from itertools import pairwise
from collections import Counter, defaultdict
from copy import deepcopy

def find_dijkstra(risk_min, grid, start_y, start_x, end_y, end_x, risk_cur):
    visited = []
    unvisited = []
    for y in range(end_y+1):
        for x in range(end_x+1):
            unvisited.append((y,x))
    

def find_path(risk_min, grid, start_y, start_x, end_y, end_x, risk_cur):
    if start_y == 0 and start_x == 0:
        risk=0
    else:
        risk = grid[start_y][start_x][0]
    risk_cur += risk
    grid[start_y][start_x][1] = True

    if start_y == end_y and start_x == end_x:
        if risk_min[0] > risk_cur:
            risk_min[0] = risk_cur
            print(risk_min[0], end=" ")
        print(".", end=" ")
        grid[start_y][start_x][1] = False
        risk_cur -= risk
        return

    if risk_cur < risk_min[0]:
        if start_y + 1 <= end_y and grid[start_y + 1][start_x][1] == False:
            find_path(risk_min, grid, start_y + 1, start_x, end_y, end_x, risk_cur)
        if start_x + 1 <= end_x and grid[start_y][start_x + 1][1] == False:
            find_path(risk_min, grid, start_y, start_x + 1, end_y, end_x, risk_cur)
        if start_x - 1 >= 0 and grid[start_y][start_x - 1][1] == False:
            find_path(risk_min, grid, start_y, start_x - 1, end_y, end_x, risk_cur)
        if start_y - 1 >= 0 and grid[start_y - 1][start_x][1] == False:
            find_path(risk_min, grid, start_y - 1, start_x, end_y, end_x, risk_cur)

    grid[start_y][start_x][1] = False
    risk_cur -= risk
    return


def main(input_name):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    grid = []
    for line in lines:
        grid.append([[int(risk), False] for risk in line.strip()])

    # PART 1
    risk = [999999999999999999999]
    find_path(risk, grid, 0, 0, len(grid) - 1, len(grid[0]) - 1, 0)
    print(f"The solution 1 is {risk[0]} ")
    # answer:


if __name__ == "__main__":
    main("test.txt")
