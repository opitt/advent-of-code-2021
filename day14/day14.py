# https://adventofcode.com/2021/day/14
import os
from rich import print
from itertools import pairwise
from collections import Counter

# Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result.
# What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?


def build_polymer(rules, template, steps):
    poly = template
    for _ in range(steps):
        #pairs = [f"{pair[0]}{pair[1]}" for pair in pairwise(poly)]
        #poly_pairs = [f"{pair[0]}{rules[pair]}" for pair in pairs]
        poly_pairs = [f"{pair[0]}{rules[pair]}" for pair in [f"{pair[0]}{pair[1]}" for pair in pairwise(poly)]]
        poly = "".join(poly_pairs)+ poly[-1][-1]
    elements = Counter(poly)
    common = elements.most_common(len(elements))
    el_max = common[0][1]
    el_min = common[-1][1]
    return el_max - el_min


# This polymer grows quickly. After step 5, it has length 97;
# After step 10, it has length 3073.
# After step 10, B occurs 1749 times, C occurs 298 times, H occurs 191 times, and N occurs 865 times;
# taking the quantity of the most common element (B, 1749) and subtracting the quantity of the least common element (H, 161) produces 1749 - 161 = 1588.

# Apply 10 steps of pair insertion to the polymer template and find the most and least common elements in the result.
# What do you get if you take the quantity of the most common element and subtract the quantity of the least common element?


def main(input_name):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    template = lines[0].strip()
    
    insert_rules = {k: v for k, v in [line.strip().split(" -> ") for line in lines[2:]]}

    # PART 1
    result = build_polymer(insert_rules, template, 10)
    print(f"The solution 1 is {result} ")
    # answer: 3058

    # PART 2
    result = build_polymer(insert_rules, template, 40)
    print(f"The solution 2 is {result} ")
    # answer:


if __name__ == "__main__":
    main("test.txt")
