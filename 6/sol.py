PACKET = 4
MESSAGE = 14

def find_start_of(distinct_characters: int) -> int:
    with open("data", "r") as f:
        data = f.read()
        for i in range(len(data)-distinct_characters-1): 
            if len(data[i:i+distinct_characters]) == len(set(list(data[i:i+distinct_characters]))): return i+distinct_characters

print(f"Part One: {find_start_of(PACKET)}")
print(f"Part Two: {find_start_of(MESSAGE)}")
