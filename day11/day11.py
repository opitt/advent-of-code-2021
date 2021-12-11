# https://adventofcode.com/2021/day/11
import os
from rich import print
from copy import deepcopy
import day11_gif as d11gif

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
        next_y, next_x = current_y + dir_y, current_x + dir_x
        if 0 <= next_y <= MAXY_IDX and \
           0 <= next_x <= MAXX_IDX:
            energy_map[next_y][next_x] += 1

def simulate_one_step(energy_map):
    # (An octopus can only flash at most once per step.)
    flashed = []
    # First, the energy level of each octopus increases by 1.
    for y, row in enumerate(energy_map):
        for x, e in enumerate(row):
            energy_map[y][x] = e + 1
    # This process continues as long as new octopuses keep having their energy level increased beyond 9.
    again=True
    while again:
        again=False
        # collect the energy from all flashing octopus that needs to be spread at the end
        # Then, any octopus with an energy level greater than 9 flashes.
        for y, row in enumerate(energy_map):
            for x, e in enumerate(row):
                if e > 9 and (y,x) not in flashed:
                    # spread energy for all adjacent octopuses 
                    spread_energy(energy_map, y, x)
                    flashed.append((y,x))
                    again=True
    # reset the energy of all octopus, that did flash
    for y,x  in flashed:
        energy_map[y][x] = 0
    return len(flashed), len(flashed) == (MAXX_IDX + 1) * (MAXY_IDX + 1)


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
        if all_flashed:
            break
    return s


def simulate_gif(energy_map, steps, filepath, filename):
    maps = list()
    maps.append(deepcopy(energy_map))
    for _ in range(steps):
        simulate_one_step(energy_map)
        maps.append(deepcopy(energy_map))
    d11gif.generate_gif(maps, 50, filepath, filename)


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

    simulate_gif(deepcopy(energy_map), 399, script_path, "simulation")


if __name__ == "__main__":
    main("input.txt")
