stack1 = "PFMQWGRT"
stack2 = "HFR"
stack3 = "PZRVGHSD"
stack4 = "QHPBFWG"
stack5 = "PSMJH"
stack6 = "MZTHSRPL"
stack7 = "PTHNML"
stack8 = "FDQR"
stack9 = "DSCNLPH"
stack_map = {
    "1": stack1,
    "2": stack2,
    "3": stack3,
    "4": stack4,
    "5": stack5,
    "6": stack6,
    "7": stack7,
    "8": stack8,
    "9": stack9
}
with open("data", "r") as f:
    data = f.read()

data_arr = data.split("\n")


def parse_instruction(instruction):
    i_comp = instruction.split(" ")
    _move = i_comp[1]
    _from = i_comp[3]
    _to = i_comp[5]
    return (_move, _from, _to)
    print(i_comp)


def move_from_to(move, from_num, to_num):
    print("------input-------")
    print(move + " " + from_num + " " + to_num)
    print("------lists-------")
    print(from_num + ": " + stack_map[from_num])
    print(to_num + ": " + stack_map[to_num])

    #print("-----CRATE 2: " + stack_map["2"])
    from_crate = list(stack_map[from_num])
    to_crate = list(stack_map[to_num])

    # take off from crate
    to_append = []
    for _ in range(int(move)):
        to_append.append(from_crate.pop())

    stack_map[from_num] = ''.join(from_crate)

    to_crate.extend(to_append)
    stack_map[to_num] = ''.join(to_crate)

    print(to_crate)
    # put on to crate
    print(to_append)

z = 0
for stuff in data_arr:
    z += 1
    print("***********8")
    print(f"z: {z}")
    print("***********8")

    _move, _from, _to = parse_instruction(stuff)
    move_from_to(_move, _from, _to)

answer = ""
for i in range(1, 10):
    answer += stack_map[str(i)][-1]

print("*********")
print(answer)
