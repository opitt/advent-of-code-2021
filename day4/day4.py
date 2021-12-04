# https://adventofcode.com/2021/day/4
import os
from rich import print
from more_itertools import flatten


def solve1(boards, draws):

    def mark_boards(boards,boards_marked,n):
        for i,board in enumerate(boards):
            if n in board:
                boards_marked[i][board.index(n)] = n
        pass

    def check_bingo(boards_marked):
        bingo_board=None
        for i,board in enumerate(boards_marked):
            hori = any(all(map(lambda n: n!=None, board[row:row+5])) for row in range(0,25,5))
            if hori:
                bingo_board=i
                break
            verti = any(all(map(lambda n: n!=None, board[col:25:5])) for col in range(5))
            if verti:
                bingo_board=i
                break
        return bingo_board 

    def calc_score(board,marked,last_num):
        # Start by finding the sum of all unmarked numbers on that board    
        res= sum(map(lambda bm: bm[0] if bm[1]==None else 0,zip(board,marked)))
        # multiply it with the last number that made the bingo
        return res * last_num

    # find the first bingo board
    boards_marked = [[None]*25 for _ in range(len(boards))]
    for num in draws:
        mark_boards(boards,boards_marked,num)
        bingo_board=check_bingo(boards_marked)
        if bingo_board != None:
            last_num=num
            break
    # The score of the winning board can now be calculated. 
    return calc_score(boards[bingo_board],boards_marked[bingo_board],last_num) 


def solve2(b, d):
    return 0


def main():
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "input.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    game = list(map(str.strip, lines))
    draws = list(map(int, game[0].split(",")))
    pos = 2
    boards = []
    while pos < len(game):
        boards.append(list(flatten([list(map(int, line.split())) for line in game[pos : pos + 5]])))
        pos+=5+1

    # PART 1
    result = solve1(boards, draws)
    print(f"The solution 1 is {result} ")
    # answer: 8580

    # PART 2
    result = solve2(boards, draws)
    print(f"The solution 2 is {result} ")
    # answer:


main()
