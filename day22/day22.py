# https://adventofcode.com/2021/day/17
import os
from rich import print


def solve1(steps):
    cubes_on = set()

    for step in steps:
        state, X, Y, Z = step["state"], step["x"], step["y"], step["z"]
        for x in range(X[0], X[1] + 1):
            for y in range(Y[0], Y[1] + 1):
                for z in range(Z[0], Z[1] + 1):
                    if state:
                        cubes_on.add((x, y, z))
                    else:
                        try:
                            cubes_on.remove((x, y, z))
                        except KeyError:
                            pass

    return len(cubes_on)


def main(input_name):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    # reboot steps: on x=10..12,y=10..12,z=10..12
    steps = []
    for line in lines:
        state, line = line.strip().split()
        x, y, z = line.split(",")
        xmin, xmax = map(int, x[2:].split(".."))
        ymin, ymax = map(int, y[2:].split(".."))
        zmin, zmax = map(int, z[2:].split(".."))
        steps.append(
            {
                "state": state == "on",
                "x": (xmin, xmax),
                "y": (ymin, ymax),
                "z": (zmin, zmax),
            }
        )
    res = solve1(steps)
    print(f"Result 1: {res}")


if __name__ == "__main__":
    # main("input.txt")
    main("test.txt")
