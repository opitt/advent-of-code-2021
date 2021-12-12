# https://adventofcode.com/2021/day/11
import os
from rich import print
from copy import deepcopy
from collections import defaultdict, Counter

# Your goal is to find the number of distinct paths that start at start, end at end,
# and don't visit small caves more than once.
# There are two types of caves: big caves (written in uppercase, like A)
# and small caves (written in lowercase, like b).
# It would be a waste of time to visit any small cave more than once,
# but big caves are large enough that it might be worth visiting them multiple times.
# So, all paths you find should visit small caves at most once, and can visit big caves any number of times.

PATHS = []


def find_paths(MAZE, current_path):
    global PATHS
    cave = current_path[-1]
    if cave == "end":
        PATHS.append(deepcopy(current_path))
        return
    maze = deepcopy(MAZE)
    caves_to = maze[cave][:]
    if cave.islower():
        maze.pop(cave)
    for cave_to in caves_to:
        current_path.append(cave_to)
        find_paths(maze, current_path)
        current_path.pop()  # remove last element
    return


# Specifically, big caves can be visited any number of times,
# a single small cave can be visited at most twice,
# and the remaining small caves can be visited at most once.
# However, the caves named start and end can only be visited exactly once each:
# once you leave the start cave, you may not return to it,
# and once you reach the end cave, the path must end immediately.
def is_smallcave(c):
    return c.islower() and c not in ("start", "end")

def is_validpath(path):
    small_caves = [c for c in path if is_smallcave(c)]
    small_cave_counter = Counter(small_caves)
    ret1 = all(map(lambda v: v <=2 , small_cave_counter.values()))
    ret2 = list(small_cave_counter.values()).count(2) <= 1
    return ret1 and ret2

def find_paths2(MAZE, current_path):
    global PATHS
    if not is_validpath(current_path):
        return
    cave = current_path[-1]
    if cave == "end":
        PATHS.append(deepcopy(current_path))
        return
    maze = deepcopy(MAZE)
    for cave_to in maze[cave]:
        current_path.append(cave_to)
        find_paths2(maze, current_path)
        current_path.pop()  # remove last element
    return


def main(input_name):
    maze = defaultdict(list)
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    for line in lines:
        cave_from, cave_to = line.strip().split("-")
        if cave_to != "start":
            maze[cave_from].append(cave_to)
        if cave_from != "start":
            maze[cave_to].append(cave_from)
    maze.pop("end")

    # PART 1
    global PATHS
    PATHS = []
    find_paths(maze, ["start"])
    result = len(PATHS)
    print(f"The solution 1 is {result} ")
    # answer: 3230

    # PART 2
    PATHS = []
    find_paths2(maze, ["start"])
    result = len(PATHS)
    print(f"The solution 2 is {result} ")
    # answer: 83475


if __name__ == "__main__":
    main("input.txt")
