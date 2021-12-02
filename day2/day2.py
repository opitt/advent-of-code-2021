# https://adventofcode.com/2021/day/2
import os

def solve1(cmds):
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
    ret = None
    return ret

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
        f"The depth*position is {result} "
    )
    # answer: 1727785422

main()
