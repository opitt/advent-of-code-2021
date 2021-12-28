# https://adventofcode.com/2021/day/25
import os
from rich import print
from copy import deepcopy

SWARM_E = ">"
SWARM_S = "v"
SWARM_X_MAX = 0
SWARM_Y_MAX = 0


def print_swarms(swarms):
    grid = []
    for _ in range(SWARM_Y_MAX + 1):
        grid.append(list("." * (SWARM_X_MAX + 1)))
    for y, x in swarms[SWARM_E].keys():
        grid[y][x] = SWARM_E
    for y, x in swarms[SWARM_S].keys():
        grid[y][x] = SWARM_S
    for row in grid:
        print("".join(row))
    print("")


def move_one_step(swarms):
    # can east swarm move?
    move_east = 0
    new_pos = {}
    for y, x in swarms[SWARM_E].keys():
        y_new = y
        x_new = x + 1 if x < SWARM_X_MAX else 0
        if swarms[SWARM_E].get((y_new, x_new), (-1, -1)) == (-1, -1) and swarms[
            SWARM_S
        ].get((y_new, x_new), (-1, -1)) == (-1, -1):
            # nothing in the way, cucumber can move
            move_east += 1
        else:
            x_new = x
        new_pos[(y_new, x_new)] = SWARM_E
    if move_east:swarms[SWARM_E] = deepcopy(new_pos)

    # can south swarm move?
    move_south = 0
    new_pos = {}
    for y, x in swarms[SWARM_S].keys():
        y_new = y + 1 if y < SWARM_Y_MAX else 0
        x_new = x
        if swarms[SWARM_E].get((y_new, x_new), (-1, -1)) == (-1, -1) and swarms[
            SWARM_S
        ].get((y_new, x_new), (-1, -1)) == (-1, -1):
            # nothing in the way, cucumber can move
            move_south += 1
        else:
            y_new = y
        new_pos[(y_new, x_new)] = SWARM_S
    if move_south:swarms[SWARM_S] = deepcopy(new_pos)

    return move_east + move_south


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
    swarms = {SWARM_E: {}, SWARM_S: {}}
    for y, line in enumerate(lines):
        scan = line.strip()
        for x, cucumber in enumerate(scan):
            if cucumber != ".":
                swarms[cucumber][(y, x)] = cucumber
    global SWARM_X_MAX, SWARM_Y_MAX
    SWARM_X_MAX = x
    SWARM_Y_MAX = y

    res = solve1(swarms)
    print(f"Result 1: {res}")  #


if __name__ == "__main__":
    main("input.txt")
