# https://adventofcode.com/2021/day/14
import os
from rich import print
from itertools import pairwise
from collections import Counter, defaultdict
from copy import deepcopy


def find_dijkstra(grid, end_y, end_x):
    MAXDIST=9999999999999999999999999999999999999999
    risk=0
    visited = {}
    unvisited = {}
    vertex = {}
    for y in range(end_y + 1):
        for x in range(end_x + 1):
            unvisited[(y, x)] = (y,x)
            vertex[(y, x)] = {"dist": MAXDIST,
                              "prev": None}
    vertex[(0, 0)]["dist"] = 0 # grid[0][0]

    while len(unvisited):
        # find unvisited vertex with smallest distance
        v_min=min(unvisited.keys())
        for v in unvisited:
            if vertex[v]["dist"] < vertex[v_min]["dist"]:
                v_min = v
        
        # examine unvisited neighbours
        v_min_dist=vertex[v_min]["dist"]
        y,x=v_min
        if y + 1 <= end_y and unvisited.get((y+1,x),False):
            dist = grid[y+1][x]
            if v_min_dist+dist < vertex[(y+1,x)]["dist"]:
                vertex[(y+1,x)]["dist"] = v_min_dist + dist
                vertex[(y+1,x)]["prev"] = v_min 
        if x + 1 <= end_x and unvisited.get((y,x+1),False):
            dist = grid[y][x+1]
            if v_min_dist+dist < vertex[(y,x+1)]["dist"]:
                vertex[(y,x+1)]["dist"] = v_min_dist + dist
                vertex[(y,x+1)]["prev"] = v_min 
        if y - 1 >= 0 and unvisited.get((y-1,x),False):
            dist = grid[y-1][x]
            if v_min_dist+dist < vertex[(y-1,x)]["dist"]:
                vertex[(y-1,x)]["dist"] = v_min_dist + dist
                vertex[(y-1,x)]["prev"] = v_min 
        if x - 1 >= 0 and unvisited.get((y,x-1),False):
            dist = grid[y][x-1]
            if v_min_dist+dist < vertex[(y,x-1)]["dist"]:
                vertex[(y,x-1)]["dist"] = v_min_dist + dist
                vertex[(y,x-1)]["prev"] = v_min 
        # mark vertext as visited
        visited[v_min]=v_min 
        unvisited.pop(v_min)     

    risk=vertex[(end_y,end_x)]["dist"] # distance
    return risk


def main(input_name):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    grid = []
    for line in lines:
        grid.append([int(risk) for risk in line.strip()])

    # PART 1
    result = find_dijkstra( grid, len(grid) - 1, len(grid[0]) - 1)
    print(f"The solution 1 is {result} ")
    # answer: 790

    # PART 2
    big_grid=[]
    plus = lambda row,n: [v+n if (v+n)<=9 else (v+n)-9 for v in row]
    for row in grid:
        big_grid.append(plus(row,0) + plus(row,1) + plus(row,2) + plus(row,3) + plus(row,4))
    grid=[]
    for row in big_grid:
        grid.append(plus(row,0))
    for row in big_grid:
        grid.append(plus(row,1))
    for row in big_grid:
        grid.append(plus(row,2))
    for row in big_grid:
        grid.append(plus(row,3))
    for row in big_grid:
        grid.append(plus(row,4))

    result = find_dijkstra( grid, len(grid) - 1, len(grid[0]) - 1)
    print(f"The solution 2 is {result} ")
    # answer: 

if __name__ == "__main__":
    main("input.txt")
