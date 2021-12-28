# https://adventofcode.com/2021/day/25
import os
from rich import print
from collections import defaultdict
from copy import deepcopy

SWARM_E = ">"
SWARM_S = "v"
SWARM_X_MAX = 0
SWARM_Y_MAX = 0


def print_swarms(swarms):
    grid = []
    for _ in range(SWARM_Y_MAX + 1):
        grid.append(list("." * (SWARM_X_MAX + 1)))
    for y, x in swarms[SWARM_E]:
        grid[y][x] = SWARM_E
    for y, x in swarms[SWARM_S]:
        grid[y][x] = SWARM_S
    for row in grid:
        print("".join(row))
    print("")


def move_one_step(swarms):
    moves_east = moves_south = 0
    new_pos = []
    # can east swarm move?
    for y, x in swarms[SWARM_E]:
        x_new = x + 1 if x < SWARM_X_MAX else 0
        if (y, x_new) in swarms[SWARM_E] or (y, x_new) in swarms[SWARM_S]:
            # can't move this cucumber
            new_pos.append((y, x))
        else:
            moves_east += 1
            new_pos.append((y, x_new))
    if moves_east:
        swarms[SWARM_E] = new_pos[:]
    # can south swarm move?
    new_pos = []
    for y, x in swarms[SWARM_S]:
        y_new = y + 1 if y < SWARM_Y_MAX else 0
        if (y_new, x) in swarms[SWARM_E] or (y_new, x) in swarms[SWARM_S]:
            # can't move this cucumber
            new_pos.append((y, x))
        else:
            moves_south += 1
            new_pos.append((y_new, x))
    if moves_south:
        swarms[SWARM_S] = new_pos[:]

    return moves_east + moves_south


def solve1(swarms):
    steps = 0
    #print_swarms(swarms)
    while True:
        steps += 1
        moves = move_one_step(swarms)
        #print_swarms(swarms)
        print(f"Round {steps}: {moves} moves")
        if moves == 0:
            break
    return steps


def main(input_name):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    swarms = {SWARM_E: [], SWARM_S: []}
    for y, line in enumerate(lines):
        scan = line.strip()
        for x, cucumber in enumerate(scan):
            if cucumber != ".":
                swarms[cucumber].append((y, x))
    global SWARM_X_MAX, SWARM_Y_MAX
    SWARM_X_MAX = x
    SWARM_Y_MAX = y

    res = solve1(swarms)
    print(f"Result 1: {res}")  #


if __name__ == "__main__":
    main("input.txt")
