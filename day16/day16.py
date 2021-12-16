# https://adventofcode.com/2021/day/16
import os
from rich import print


def decode_literal_value(decoded, bits):
    # Literal value packets encode a single binary number. To do this, the binary number is padded with leading zeroes until its length is a multiple of four bits, 
    # and then it is broken into groups of four bits. 
    # Each group is prefixed by a 1 bit except the last group, which is prefixed by a 0 bit. These groups of five bits immediately follow the packet header. 
    # For example, the hexadecimal string D2FE28 becomes: 110100101111111000101000
    #                                                     VVVTTTAAAAABBBBBCCCCC
    literal_value = ""
    while True:
        group=bits[:5]
        bits=bits[5:]
        literal_value+=group[1:]
        if group[0]=="0":break
    literal_value=int(literal_value,2) # 2021 for test
    decoded.append({f"value":literal_value})
    return decoded, bits

def decode_operator(decoded, bits, operator_id):
    ops={ 0:"sum", 1:"*", 2:"min", 3:"max", 5:">", 6:"<", 7:"==" }
    
    # Every other type of packet (any packet with a type ID other than 4) represent an operator that performs some calculation on one or more sub-packets contained within. 
    # Right now, the specific operations aren't important; focus on parsing the hierarchy of sub-packets.
    # An operator packet contains one or more packets. 
    # To indicate which subsequent binary data represents its sub-packets, 
    #     an operator packet can use one of two modes indicated by the bit immediately after the packet header; this is called the length type ID:
    #   - If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
    #   - If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
    p_length_type_id=bits[0]
    bits=bits[1:]
    if p_length_type_id=="0":
        p_total_length_of_subpackets=int(bits[:15],2)
        bits=bits[15:]
        decoded.append({"op":f"{ops[operator_id]}","id":operator_id,"open":"("})
        sub_bits=bits[:p_total_length_of_subpackets]
        while len(sub_bits):
            decoded, sub_bits = decode_nextpacket(decoded, sub_bits)
        decoded.append({"id":operator_id,"close":")"})
        bits=bits[p_total_length_of_subpackets:]        
    else:
        p_number_of_subpackets=int(bits[:11],2)
        bits=bits[11:]
        decoded.append({"op":f"{ops[operator_id]}","id":operator_id,"open":"(","args":p_number_of_subpackets})
    return decoded, bits

    # Finally, after the length type ID bit and the 15-bit or 11-bit field, the sub-packets appear.
    
    # An operator packet contains one or more packets. 
    # To indicate which subsequent binary data represents its sub-packets, 
    # an operator packet can use one of two modes indicated by the bit immediately after the packet header; 
    # this is called the length type ID:

def decode_nextpacket(decoded, bits):
    # Every packet begins with a standard header: the first three bits encode the packet version, and the next three bits encode the packet type ID.
    # These two values are numbers; all numbers encoded in any packet are represented as binary with the most significant bit first. 
    # For example, a version encoded as the binary sequence 100 represents the number 4.
    p_version = int(bits[:3], 2)
    decoded.append({"version":p_version})
    p_type_id = int(bits[3:6], 2)
    bits = bits[6:]
    match p_type_id:
        case 4:
            # Packets with type ID 4 represent a literal value. 
            decoded, bits = decode_literal_value(decoded,bits)
        case _:
            # operator packets
            decoded, bits = decode_operator(decoded,bits,p_type_id)
    return decoded, bits

def decode_transmission(transmission):
    decoded =[]
    # The BITS transmission contains a single packet at its outermost layer which itself contains many other packets. 
    # The hexadecimal representation of this packet might encode a few extra 0 bits at the end; these are not part of the transmission and should be ignored.
    bits = "".join([f"{int(c,16):04b}" for c in transmission])
    while len(bits)!=bits.count("0"):
        decoded, bits = decode_nextpacket(decoded, bits)
    return sum( d.get("version",0) for d in decoded), decoded

def calculate(decoded):
    ops=[]
    for d in decoded:
        ops.extend([d.get("op",""), d.get("open",""), "#"+str(d.get("args","")) if d.get("args",0)>0 else "", d.get("close",""), str(d.get("value",""))])
    print(" ".join(o for o in ops if len(o)))

def main(input_name,use_line=0):
    # READ INPUT FILE
    script_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(script_path, input_name), encoding="utf-8") as input:
        lines = input.readlines()

    transmission = [line.strip() for line in lines][use_line]

    # PART 1
    result, decoded = decode_transmission(transmission)
    print(f"The solution 1 is {result} ")
    # answer: 986

    # PART 2
    result = calculate(decoded)
    print(f"The solution 2 is {result} ")
    # answer: 


if __name__ == "__main__":
    main("test.txt",4) # result: 12
    main("test.txt",5) # result: 23
    main("test.txt",6) # result: 31
    main("input.txt")  # result: 986 
    
