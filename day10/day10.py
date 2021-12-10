# https://adventofcode.com/2021/day/10
import os
from rich import print
from copy import deepcopy

# A corrupted line is one where a chunk closes with the wrong character -
# that is, where the characters it opens and closes with do not form one
# of the four legal pairs listed above.
# Examples of corrupted chunks include (], {()()()>, (((()))}, and <([]){()}[{}]).
# Such a chunk can appear anywhere within a line, and its presence causes the whole
# line to be considered corrupted


def score_code(line):
    score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    score2 = {"(": 1, "[": 2, "{": 3, "<": 4}
    l=0
    while l != len(line):
        l = len(line)
        line = (
            line.replace("()", "").replace("{}", "").replace("[]", "").replace("<>", "")
        )
    if len == 0:
        # correct
        return 0  
    elif sum(map(lambda c: c in ")}>]", line)) > 0:
        # corrupt (use positive return score)
        line = line.replace("(", "").replace("{", "").replace("[", "").replace("<", "")
        return score[line[0]]  
    else: 
        # incomplete (use negative return score)
        line_score = 0
        for c in line[::-1]:
            line_score *= 5
            line_score += score2[c]
        return -line_score


def solve1(code):
    scores = [score_code(line[:]) for line in code]
    return sum(filter(lambda x: x > 0, scores))

def solve2(code):
    scores = [score_code(line[:]) for line in code]
    scores = sorted(list(filter(lambda x: x < 0, scores)))
    score = -scores[len(scores) // 2]
    return score


def main(input_name):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    code = [line.strip() for line in lines]

    result = solve1(deepcopy(code))
    print(f"The solution 1 is {result} ")
    # answer:315693

    result = solve2(deepcopy(code))
    print(f"The solution 2 is {result} ")
    # answer:1870887234


if __name__ == "__main__":
    main("input.txt")
