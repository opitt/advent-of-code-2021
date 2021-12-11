# https://adventofcode.com/2021/day/11
import os
from rich import print
from copy import deepcopy

# First, the energy level of each octopus increases by 1.

# Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of all adjacent octopuses by 1,
# including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes.
# This process continues as long as new octopuses keep having their energy level increased beyond 9.
# (An octopus can only flash at most once per step.)

# Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.


def spread_energy(energy_map, current_y, current_x):
    for dir_y, dir_x in [
        (1, 1),
        (1, 0),
        (1, -1),
        (0, 1),
        (0, -1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
    ]:
        next_y = current_y + dir_y
        next_x = current_x + dir_x
        if 0 <= next_y <= MAXY_IDX and 0 <= next_x <= MAXX_IDX:
            energy_map[next_y][next_x] += 1
    return energy_map


def simulate_one_step(energy_map):
    # (An octopus can only flash at most once per step.)
    flashed_map = [[0] * (MAXX_IDX + 1) for _ in range(MAXY_IDX + 1)]

    # First, the energy level of each octopus increases by 1.
    for y, row in enumerate(energy_map):
        for x, e in enumerate(row):
            energy_map[y][x] = e + 1

    # This process continues as long as new octopuses keep having their energy level increased beyond 9.
    while True:
        # collect the energy from all flashing octopus that needs to be spread at the end
        spreadenergy_map = [[0] * (MAXX_IDX + 1) for _ in range(MAXY_IDX + 1)]
        flash_count = 0
        # Then, any octopus with an energy level greater than 9 flashes.
        for y, row in enumerate(energy_map):
            for x, e in enumerate(row):
                if e > 9 and flashed_map[y][x] == 0:
                    # spread energy for all adjacent octopuses ... and save it
                    spreadenergy_map = spread_energy(spreadenergy_map, y, x)
                    flashed_map[y][x] = 1
                    flash_count += 1
        if flash_count == 0:
            break
        # now spread the energy created by flashing octopus to all effected octopuses
        for y, row in enumerate(spreadenergy_map):
            for x, e in enumerate(row):
                energy_map[y][x] += e

    # reset the energy of all octopus, that did flash, to 0
    total_flashes = 0
    for y, row in enumerate(flashed_map):
        for x, f in enumerate(row):
            total_flashes += f
            if f == 1:
                energy_map[y][x] = 0

    return total_flashes, total_flashes == (MAXX_IDX + 1) * (MAXY_IDX + 1)


def print_map(energy_map):
    for row in energy_map:
        print(*row, sep="")
    print("")


def get_flashes_after_steps(energy_map, steps):
    flashes = 0
    for s in range(1, steps + 1):
        flashed, _ = simulate_one_step(energy_map)
        flashes += flashed
    return flashes

def get_steps_to_allflashed(energy_map):
    s = 0
    while True:
        s += 1
        _, all_flashed = simulate_one_step(energy_map)
        if all_flashed:break
    return s

MAXX_IDX = 0
MAXY_IDX = 0

def main(input_name):
    # READ INPUT FILE
    global MAXX_IDX, MAXY_IDX
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    energy_map = [list(map(int, line.strip())) for line in lines]
    MAXX_IDX = len(energy_map[0]) - 1
    MAXY_IDX = len(energy_map) - 1

    result = get_flashes_after_steps(deepcopy(energy_map), 100)
    print(f"The solution 1 is {result} ")
    # answer: 1599

    result = get_steps_to_allflashed(deepcopy(energy_map))
    print(f"The solution 2 is {result} ")
    # answer: 418


if __name__ == "__main__":
    main("input.txt")
