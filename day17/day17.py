# https://adventofcode.com/2021/day/17
import os
from rich import print

def main(input_name,use_line=0):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    # target area: x=20..30, y=-10..-5
    line=lines[use_line]
    x,y=line[line.find(":")+2:].split()
    x1,x2 = map(int,x.replace(",","").split("=")[1].split(".."))
    y1,y2 = map(int,y.split("=")[1].split(".."))

    pass
if __name__ == "__main__":
    for i in range(1):
        main("test.txt",i) 
    #main("input.txt")
    
