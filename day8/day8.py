# https://adventofcode.com/2021/day/8
import os
from rich import print
import itertools as it
from copy import deepcopy

def display_print(signal):
    placeholders="abcdefg"
    D=[
        " aaaa ", 
        "b    c",
        "b    c", 
        " dddd ", 
        "e    f", 
        "e    f", 
        " gggg "]
    out=[segment.replace(letter, "#" if sig!=" " else " ") for sig,letter in zip(signal,placeholders) for segment in D]
    #for segment in D:
    #    for sig,letter in zip(signal,placeholders):
    #        segment= segment.replace(letter, "#" if sig!=" " else " ")
    #    out.append(segment)
    print("\n".join(out))

        
def solve(sig_patterns):
    segment_options=list("".join(p) for p in it.permutations('abcdefg', 7))
    seg_template={
        1:"  1  1 ",  # 1
        7:"1 1  1 ",  # 7
        3:"1 11 11",  
        4:" 111 1 ",  # 4
        0:"111 111",  # abcdefg
        5:"11 1 11",
        6:"11 1111",
        2:"1 111 1",  
        8:"1111111",  # 8
        9: "1111 11"}

    for sig in sig_patterns:
        


    options=[[] for _ in range(10)]
    for sig in sig_patterns:
        for n, templ in seg_template.items():
            if templ.count("1")==len(sig):
                for s in it.permutations(sig,len(sig)):
                    t=templ
                    for c in s:
                        t=t.replace("1",c,1)
                    options[n].append(t)
                    display_print(t)


    # start with 1
    

    pass

def filter_(options,filter_on_idx):
    options_filtered=[[] for _ in range(10)]
    for o in options[filter_on_idx]:
        # remove all options, that do not match
        for i in range(9):
            options_filtered[i].extend([opt for opt in options[i] if is_partof(o,opt)])
    options_filtered[filter_on_idx]=options[filter_on_idx][:]
    return deepcopy(options_filtered)

def is_partof(ref, tst):
    return all(r==t or r==" " or t==" " for r,t in zip(ref,tst))

def main(part=0):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, "test.txt"), encoding="utf-8") as input:
        lines = input.readlines()
    #
    sig_patterns = [
        list(map("".join, map(sorted, line.split(" | ")[0].split()))) for line in lines
    ]
    digit_output = [
        list(map("".join, map(sorted, line.split(" | ")[1].split()))) for line in lines
    ]

    # PART 1
    if 1 in part:
        result = sum(
            [
                sum(map(lambda d: 1 if len(d) in (2, 4, 7, 3) else 0, digi))
                for digi in digit_output
            ]
        )
        print(f"The solution 1 is {result} ")
        # answer: 318

    # PART 2
    if 2 in part:
        result = solve(sig_patterns[0])
        print(f"The solution 2 is {result} ")
        # answer:


if __name__ == "__main__":
    main([2])
    # t = timeit.Timer(lambda: main([2]))
    # print(t.timeit(1),"sec")
