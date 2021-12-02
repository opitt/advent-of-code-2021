# https://adventofcode.com/2021/day/2
import os
from rich import print

def solve1(cmds):
    """calculate the depth and position by applying the given commands
    logic: up/down change the depth; forward changes position

    Args:
        cmds (list): list of a command and one value: e.g. forward 5

    Returns:
        int: magic number for AOC
    """
    depth,pos=0,0
    for c in cmds:
        dir,val=c.split()
        val=int(val)
        match dir:
            case "forward":
                pos+=val
            case "up":
                depth-=val
            case "down":
                depth+=val
    return depth*pos

def solve2(cmds):
    """calculate the depth and position by applying the given commands
    logic: up/down change the aim; forward changes position AND depth

    Args:
        cmds (list): list of a command and one value: e.g. forward 5

    Returns:
        int: magic number for AOC
    """
    depth,pos,aim=0,0,0
    for c in cmds:
        dir,val=c.split()
        val=int(val)
        match dir:
            case "forward":
                pos+=val
                depth+=aim*val
            case "up":
                aim-=val
            case "down":
                aim+=val
    return depth*pos

def main():
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input.txt"), encoding="utf-8") as input:
        commands = input.readlines()
    commands = list(map(str.strip, commands))

    # PART 1
    result=solve1(commands)
    print(
        f"The depth*position is {result} "
    )
    # answer: 1840243

    # PART 2
    result = solve2(commands)
    print(
        f"The depth*position using aim logic is {result} "
    )
    # answer: 1727785422

main()
