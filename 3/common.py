def calc_priority(letter):
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = lowercase.upper()

    if letter in lowercase:
        return lowercase.index(letter) + 1
    else:
        return uppercase.index(letter) + 26 + 1

print(calc_priority("s"))