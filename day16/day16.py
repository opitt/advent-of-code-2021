# https://adventofcode.com/2021/day/16
import os
from rich import print
import queue as q


def decode_stream(cur_op_q,cur_params_q, bits_remaining):
    OPS={ 0:"add", 1:"mult", 2:"mi", 3:"ma", 5:"gt", 6:"lt", 7:"eq", 4:"val" }

    while len(bits_remaining)!=bits_remaining.count("0"):
        cur_op, cur_need=cur_op_q.get()
        cur_params=cur_params_q.get()

        if len(cur_params)<cur_need or cur_need<0:
            # decode next block, need more parameters for the operator
            cur_params_q.put(cur_params)
            cur_op_q.put((cur_op,cur_need))
        elif len(cur_params)==cur_need:
            # merge the parameters with their operator
            cur_params=cur_op + "("+ ",".join(cur_params) + ")"
            # append operand with parameters as parameter - one level higher
            p=cur_params_q.get()
            p.append(cur_params)
            cur_params_q.put(p)
            continue
            # decode next block ...
        else:
            raise ValueError
            
        p_version, p_type_id = int(bits_remaining[:3], 2), int(bits_remaining[3:6], 2)
        bits_remaining = bits_remaining[6:]
        match p_type_id:
            case 0 | 1 | 2 | 3 | 5 | 6 | 7:
                # operator packets
                p_length_type_id=bits_remaining[0]
                bits_remaining=bits_remaining[1:]
                if p_length_type_id=="0":
                    p_total_length_of_subpackets=int(bits_remaining[:15],2)
                    bits_remaining=bits_remaining[15:]
                    sub_packetbits=bits_remaining[:p_total_length_of_subpackets]

                    cur_op_q.put((OPS[p_type_id],-1))
                    cur_params_q.put([])

                    decode_stream(cur_op_q,cur_params_q, sub_packetbits)
                    bits_remaining=bits_remaining[p_total_length_of_subpackets:]        
                else:
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
                raise ValueError

    cur_op,cur_need=cur_op_q.get()
    if cur_op!= "print":
        cur_params=cur_params_q.get()
        para_up=cur_params_q.get() # the next higher level
        para_up.append(cur_op + "("+ ",".join(cur_params) + ")")
        cur_params_q.put(para_up)
    else:
        cur_op_q.put((cur_op,cur_need))
    return
    

def calculate(decoded):
    import queue as q
    ops=[]
    args=0
    q_ops=q.LifoQueue()
    q_arg=q.LifoQueue()
    
    for d in decoded:
        match d:
            case {"op":op, "open":_}:
                ops.append(op+"(")
                q_ops.put(ops[:])
                q_arg.put(args)
                ops,args=[],0

            case {"op":op, "close":_}:
                temp=q_ops.get()
                temp.extend(ops)
                temp.append("),")
                ops=temp[:]
                args=q_arg.get()
                if args>0:
                    args-=1
                    if args==0:
                        temp=q_ops.get()
                        temp.extend(ops)
                        temp.append("),")
                        ops=temp[:]
                        args=q_arg.get()

            case {"op":op, "args":a}:
                ops.append(op+"(")
                q_ops.put(ops[:])
                q_arg.put(args)
                ops,args=[],a       
            case {"value":v}:
                ops.append(str(v)+",")
                if args>0:
                    args-=1
                    if args==0:
                        temp=q_ops.get()
                        temp.extend(ops)
                        temp.append("),")
                        ops=temp[:]
                        args=q_arg.get()

        #ops.extend([d.get("op",""), d.get("open",""), "#"+str(d.get("args","")) if d.get("args",0)>0 else "", d.get("close",""), str(d.get("value",""))])
    while not q_ops.empty():
        temp=q_ops.get()
        temp.extend(ops)
        temp.append(")")
        ops=temp[:]
        args=q_arg.get()
    pass
    res = "".join(op for op in ops)
    #res = res.replace(",)",")")
    if res[-1]==",":
        res = res[:-1]
    print(res)
    return

def mult(*args):
    import math 
    return math.prod(args)

def add(*args):
    return sum(args)

def ma(*args):
    return max(args)

def mi(*args):
    return min(args)

def gt(a,b):
    return a>b

def lt(a,b):
    return a<b

def eq(a,b):
    return a==b

def main(input_name,use_line=0):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()

    transmission = [line.strip() for line in lines][use_line]
    bits = "".join([f"{int(c,16):04b}" for c in transmission])

    # PART 1
    cur_op_q=q.LifoQueue()      # queue: (operand, parameters expected)   e.g. ("mul",2) or ("ma":-1)
    cur_params_q=q.LifoQueue()  # queue: [list of parameter strings]   e.g. ["1234","add(23,gt(1,2),4)"]
    cur_op_q.put(("print",-1))  
    cur_params_q.put([])
 
    decode_stream(cur_op_q, cur_params_q, bits)
    # now collapse the levels, nothin left to decode
    while not cur_op_q.empty():
        op, need = cur_op_q.get()
        params = cur_params_q.get()
        params = op + "(" + ",".join(params) + ")"
        if not cur_op_q.empty():
            # append parameter to above level
            p = cur_params_q.get()
            p.append(params)
            cur_params_q.put(p)
    
    # result too low: 18217411328220
    print(params)             
    exec(params,globals())


if __name__ == "__main__":
    #for i in range(7,15):
    #    main("test.txt",i) 
    main("input.txt")  # result: 986 
    
