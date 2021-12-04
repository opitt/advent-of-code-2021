# https://adventofcode.com/2021/day/4
import os
from rich import print
from more_itertools import flatten


def mark_boards(boards, boards_marked, num):
    for b, board in enumerate(boards):
        if num in board:
            boards_marked[b][board.index(num)] = num
    pass

def check_bingo(boards_marked, boards_with_bingo):
    count = 0
    for b, board in enumerate(boards_marked):
        if b in boards_with_bingo:
            continue
        hori = any(
            all(map(lambda n: n != None, board[row : row + 5]))
            for row in range(0, 25, 5)
        )
        verti = any(
            all(map(lambda n: n != None, board[col:25:5])) for col in range(5)
        )
        if verti or hori:
            boards_with_bingo.append(b)
            count += 1
    return count>0

def calc_score(board, marked, last_num):
    # Start by finding the sum of all unmarked numbers on that board
    res = sum(map(lambda bm: bm[0] if bm[1] == None else 0, zip(board, marked)))
    # multiply it with the last number that made the bingo
    return res * last_num

def solve1(boards, draws):
    # find the FIRST bingo board
    boards_marked = [[None] * 25 for _ in range(len(boards))]
    boards_with_bingo=[]
    for num in draws:
        mark_boards(boards, boards_marked, num)
        if check_bingo(boards_marked,boards_with_bingo):
            last_num = num
            break
    # The score of the winning board can now be calculated.
    return calc_score(boards[boards_with_bingo[-1]], boards_marked[boards_with_bingo[-1]], last_num)

def solve2(boards, draws):
    # find the LAST bingo board
    boards_marked = [[None] * 25 for _ in range(len(boards))]
    boards_with_bingo = []
    for num in draws:
        mark_boards(boards, boards_marked, num)
        if check_bingo(boards_marked, boards_with_bingo):
            # at least one bingo was found
            last_bingo_num = num
        if len(boards_with_bingo) == len(boards):
            # all cards have a bingo now
            break
    # The score of the winning board can now be calculated.
    return calc_score(
        boards[boards_with_bingo[-1]],
        boards_marked[boards_with_bingo[-1]],
        last_bingo_num,
    )


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
        boards.append(
            list(
                flatten([list(map(int, line.split())) for line in game[pos : pos + 5]])
            )
        )
        pos += 5 + 1
    # all_nums_distinct=all([len(set(b)) == len(b) for b in boards])

    # PART 1
    result = solve1(boards, draws)
    print(f"The solution 1 is {result} ")
    # answer: 8580

    # PART 2
    result = solve2(boards, draws)
    print(f"The solution 2 is {result} ")
    # answer: 9576


main()
