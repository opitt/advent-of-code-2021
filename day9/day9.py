# https://adventofcode.com/2021/day/9
import os
from rich import print
import itertools as it
from copy import deepcopy

def is_low(H,y,x):
    MAXY=len(H)-1
    MAXX=len(H[0])-1
    neighbours_x=[max(x-1,0),x,min(MAXX,x+1)]
    neighbours_y=[max(y-1,0),y,min(MAXY,y+1)]   
    for ny in neighbours_y:
        for nx in neighbours_x:
            if nx==x and ny==y:
                continue
            if H[y][x] >= H[ny][nx]:
                return False
    return True


def solve(H):
    lows=[]
    for y in range(len(H)):
        for x in range(len(H[0])):
            if is_low(H,y,x):
                lows.append(H[y][x])
    return sum(lows)+len(lows)

def main(part=0):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    heights = [
        list(map(int,line.strip())) for line in lines
    ]

    # PART 1
    if 1 in part:
        result = solve(heights)
        print(f"The solution 1 is {result} ")
        # answer: 444

if __name__ == "__main__":
    main([1])
    # t = timeit.Timer(lambda: main([2]))
    # print(t.timeit(1),"sec")
