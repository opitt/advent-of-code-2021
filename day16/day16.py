# https://adventofcode.com/2021/day/16
import os
from rich import print
import queue as q
import math 


def decode_packetstream(cur_op,cur_need, bits_remaining):
    OPS={ 0:"add", 1:"mult", 2:"mi", 3:"ma", 5:"gt", 6:"lt", 7:"eq", 4:"val" }
    cur_op_q=q.LifoQueue()      # queue: (operand, parameters expected)   e.g. ("mul",2) or ("ma":-1)
    cur_params_q=q.LifoQueue()  # queue: [list of parameter strings]   e.g. ["1234","add(23,gt(1,2),4)"]
    cur_op_q.put((cur_op,cur_need))
    cur_params_q.put([])
    cur_version_sum = 0

    while len(bits_remaining)!=bits_remaining.count("0"): # as long as there are bits ... except the last zero bits
        # what's the the current operator, and how many parameters are needed?
        cur_op, cur_need=cur_op_q.get()
        cur_params=cur_params_q.get()

        # check, if all parameters are gathered, or if we need to continue decoding
        if len(cur_params)<cur_need or cur_need<0:
            # need more parameters for the operator
            cur_params_q.put(cur_params)
            cur_op_q.put((cur_op,cur_need))
            # decode next block ...
        elif len(cur_params)==cur_need:
            # we as many parameters as needed for current operator
            # merge the parameters with their operator
            cur_params=cur_op + "("+ ",".join(cur_params) + ")"
            # append operand with parameters as parameter - one level higher
            p=cur_params_q.get()
            p.append(cur_params)
            cur_params_q.put(p)
            continue
        else:
            # just in case ...
            raise ValueError
            
        p_version, p_type_id = int(bits_remaining[:3], 2), int(bits_remaining[3:6], 2)
        bits_remaining = bits_remaining[6:]
        cur_version_sum += p_version # only needed for part 1 challenge

        match p_type_id:
            case 0 | 1 | 2 | 3 | 5 | 6 | 7:
                # operator packets
                p_length_type_id=bits_remaining[0]
                bits_remaining=bits_remaining[1:]
                if p_length_type_id=="0":
                    # we have to decode the next given sub bit stream
                    p_total_length_of_subpackets=int(bits_remaining[:15],2)
                    bits_remaining=bits_remaining[15:]
                    sub_packetbits=bits_remaining[:p_total_length_of_subpackets]
                    bits_remaining=bits_remaining[p_total_length_of_subpackets:]        
                    next_op=OPS[p_type_id]
                    cur_params, version=decode_packetstream(next_op,-1, sub_packetbits)
                    cur_version_sum += version
                    p=cur_params_q.get()
                    p.append(cur_params)
                    cur_params_q.put(p)

                else:
                    # we know, how many packets/parameters to decode ... 
                    p_number_of_subpackets=int(bits_remaining[:11],2)
                    bits_remaining=bits_remaining[11:]
                    cur_op_q.put((OPS[p_type_id],p_number_of_subpackets))
                    cur_params_q.put([])        
            case 4:
                # Packets with type ID 4 represent a literal value. 
                value = ""
                while True:
                    group=bits_remaining[:5]
                    bits_remaining=bits_remaining[5:]
                    value+=group[1:]
                    if group[0]=="0":break
                value=int(value,2)
                # append value to current level's parameter list
                cur_params=cur_params_q.get()
                cur_params.append(str(value))
                cur_params_q.put(cur_params)
            case _:
                # just in case
                raise ValueError

    # now the bit stream is decoded, merge the parameter stack
    while cur_op_q.qsize():
        cur_op,cur_need=cur_op_q.get()
        cur_params=cur_params_q.get()
        cur_params=cur_op + "("+ ",".join(cur_params) + ")"
        if cur_op_q.qsize():
            para_up=cur_params_q.get() # the next higher level
            para_up.append(cur_params)
            cur_params_q.put(para_up)
    return cur_params, cur_version_sum

def main(input_name,use_line=0):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()
    transmission = [line.strip() for line in lines][use_line]
    bits = "".join([f"{int(c,16):04b}" for c in transmission])

    params, version_sum =decode_packetstream("print", -1, bits)    
    print(f"Solution part 1: version sum is {version_sum}")
    # part1: 986
    print("This is the decoded operation:\n", params)
    print("This is the result of the operation:")
    exec(params,globals())
    # part2: 18234816469452

# dummy functions for executing the resulting operation
def mult(*args):return math.prod(args)
def add(*args):return sum(args)
def ma(*args):return max(args)
def mi(*args):return min(args)
def gt(a,b):return a>b
def lt(a,b):return a<b
def eq(a,b):return a==b

if __name__ == "__main__":
    #for i in range(7,15):
    #    main("test.txt",i) 
    main("input.txt")
    
