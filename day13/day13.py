# https://adventofcode.com/2021/day/13
import os
from rich import print
from copy import deepcopy
from collections import defaultdict
import timeit

# How many dots are visible after completing just the first fold instruction on your transparent paper?
def fold_it(dots, folds, part_1):

    def add(dot):
        if dot in dots_after_folding:
            pass
        else:
            dots_after_folding.append(dot)

    FOLDXY = {"y": lambda d: (d[0], fold_line - (d[1] - fold_line)),
                "x": lambda d: (fold_line - (d[0] - fold_line),d[1])}
    XY = {"x": 0, "y": 1}

    for fold_dir, fold_line in folds[:1 if part_1 else None]:
        dots_after_folding = []
        for dot in dots:
            if dot[XY[fold_dir]] < fold_line:
                add(dot)
            elif dot[XY[fold_dir]] > fold_line:
                dot = FOLDXY[fold_dir](dot)
                add(dot)
            else:
                pass  # the fold line
        dots = deepcopy(dots_after_folding)
    if not part_1:
        print_dots(dots)
    return len(dots)


def print_dots(dots):
    maxx = max([dot[0] for dot in dots])
    maxy = max([dot[1] for dot in dots])
    # try reduce with max function

    display = [[" "] * (maxx + 1) for y in range(maxy + 1)]
    for x, y in dots:
        display[y][x] = "#"
    for row in display:
        print("".join(row))


#       x
# 0123456789A
# *.**..*..*. 0
# *...*...... 1
# ......*...* 2
# *...*...... 3 y
# .*.*1.0.*** 4
# ........... 5
# ........... 6


def main(input_name):
    maze = defaultdict(list)
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    read_dots = True
    dots = []
    folds = []
    for line in lines:
        line = line.strip()
        if line == "":
            read_dots = False
            continue
        if read_dots:
            dot = tuple(map(int, line.split(",")))  # x,y
            dots.append(dot)
        else:
            fold_along, fold_num = line.split()[2].split("=")  # x=5 or  y=3
            folds.append((fold_along, int(fold_num)))

    # PART 1
    result = fold_it(dots, folds, False)
    print(f"The solution 1 is {result} ")
    # answer: 716

    # PART 2
    result = fold_it(dots, folds, True)
    print(f"The solution 2 has {result} dot. Display:")
    # answer: RPCKFBLR


if __name__ == "__main__":
    main("input.txt")
