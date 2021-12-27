# https://adventofcode.com/2021/day/24
import os
from rich import print
import multiprocessing
from more_itertools import flatten
import time
from collections import defaultdict


def find_valid_models(model_range):
    name = multiprocessing.current_process().name
    valid_models = {
        name: [n for n in model_range if len(str(n)) == sum(map(int, str(n)))]
    }
    return valid_models[name]


def solve_nomp(max_no, min_no=0):
    cpus = 1
    range_per_cpu = max_no // cpus
    ranges=[(i*range_per_cpu,i*range_per_cpu+range_per_cpu) for i in range(cpus)]
    if max_no%cpus:
        range.append(cpus*range_per_cpu,cpus*range_per_cpu+max_no%cpu)

    model_ranges = [range(a, b) for a,b in ranges]

    res = map(find_valid_models, model_ranges)

    return list(flatten(res))


# https://www.machinelearningplus.com/python/parallel-processing-python/#:~:text=The%20general%20way%20to%20parallelize,of%20Pool%20s%20parallization%20methods.
def solve_mp(max_no, min_no=0):
    cpus = multiprocessing.cpu_count()
    range_per_cpu = max_no // cpus
    ranges=[(i*range_per_cpu,i*range_per_cpu+range_per_cpu) for i in range(cpus)]
    if max_no%cpus:
        range.append(cpus*range_per_cpu,cpus*range_per_cpu+max_no%cpu)

    model_ranges = [range(a, b) for a,b in ranges]

    with multiprocessing.Pool() as pool:
        res = pool.map(find_valid_models, model_ranges)

    return list(flatten(res))


def main():
    max_number = 10_000_000
    start = time.time()
    res = solve_mp(max_number)
    end = time.time()
    print(f"{end-start:.2f}s for {max_number}: found {len(res)} numbers")
    print(sorted(res)[-10::])

    start = time.time()
    res = solve_nomp(max_number)
    end = time.time()
    print(f"{end-start:.2f}s for {max_number}: found {len(res)} numbers")
    print(sorted(res)[-10::])


if __name__ == "__main__":
    main()
