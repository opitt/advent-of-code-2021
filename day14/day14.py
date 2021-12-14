# https://adventofcode.com/2021/day/14
import os
from rich import print
from itertools import pairwise
from collections import Counter, defaultdict
from copy import deepcopy


def build_polymer(rules, template, steps):

    def count_minmax_elements(pairs):
        element_count = defaultdict(int)
        for pair in pairs.keys():
            # count only the first element of a pair (the second element is the first of the next pair)
            element_count[pair[0]] += pairs[pair]
        # add the last element
        element_count[template[-1]] += 1
        return max(element_count.values()), min(element_count.values())

    pairs = defaultdict(int)
    for pair in pairwise(template):
        pairs["".join(pair)] += 1
    
    for _ in range(steps):
        pairs_next = defaultdict(int)
        for pair, pair_count in pairs.items():
            insert = rules[pair]
            pair1, pair2 = pair[0] + insert, insert + pair[1]
            pairs_next[pair1] += pair_count
            pairs_next[pair2] += pair_count
        pairs = deepcopy(pairs_next)

    common_max, common_min = count_minmax_elements(pairs)
    return common_max - common_min


def main(input_name):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    template = lines[0].strip()

    poly_rules = {k: v for k, v in [line.strip().split(" -> ") for line in lines[2:]]}

    # PART 1
    # Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result.
    # What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?
    result = build_polymer(poly_rules, template, 10)
    print(f"The solution 1 is {result} ")
    # answer: 3058 (test: 1588)

    # PART 2
    result = build_polymer(poly_rules, template, 40)
    print(f"The solution 2 is {result} ")
    # answer: 3447389044530 (test: 2188189693529)

if __name__ == "__main__":
    main("input.txt")
