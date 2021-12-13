# https://adventofcode.com/2021/day/13
import os
from rich import print
from collections import defaultdict

# How many dots are visible after completing just the first fold instruction on your transparent paper?
def fold_it(dots, folds, end_after=None):
    def add(dot):
        if dot in dots_folded:
            pass
        else:
            dots_folded.append(dot)

    FOLDXY = {
        "y": lambda d: (d[0], fold_line - (d[1] - fold_line)),
        "x": lambda d: (fold_line - (d[0] - fold_line), d[1]),
    }
    XY = {"x": 0, "y": 1}

    for fold_dir, fold_line in folds[:end_after]:
        dots_folded = []
        for dot in dots:
            if dot[XY[fold_dir]] < fold_line:
                add(dot)
            elif dot[XY[fold_dir]] > fold_line:
                dot = FOLDXY[fold_dir](dot)
                add(dot)
            else:
                pass  # the fold line
        dots = dots_folded[:]
    return len(dots), dots


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
    result, _ = fold_it(dots, folds, 1)
    print(f"The solution 1 is {result} ")
    # answer: 716

    # PART 2
    result, folded = fold_it(dots, folds)
    print(f"The solution 2 has {result} dots:")
    print_dots(folded)
    # ###  ###   ##  #  # #### ###  #    ###
    # #  # #  # #  # # #  #    #  # #    #  #
    # #  # #  # #    ##   ###  ###  #    #  #
    # ###  ###  #    # #  #    #  # #    ###
    # # #  #    #  # # #  #    #  # #    # #
    # #  # #     ##  #  # #    ###  #### #  #


if __name__ == "__main__":
    main("input.txt")
