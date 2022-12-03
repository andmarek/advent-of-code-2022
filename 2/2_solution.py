'''
1 rock, 2 paper, 3 scissors
+ 
0 if lost, 3 if draw, 6 if won
'''
decision = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

yours_to_theirs = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}
scores = {
    "X": "1",
    "Y": "2",
    "Z": "3",
}
with open('data', 'r') as f:
    input_str = f.read()
    new_score = 0

    arr = input_str.split("\n")
    for a in arr:
        comp = a.split(" ")

        

        # NEW
        theirs = comp[0]
        match_decision = comp[1]
        new_score += decision[match_decision]

        

        if match_decision == "X":  # lose
            if theirs == "A": # rock
                new_score += 3
            elif theirs == "B":  # paper
                new_score += 1
            elif theirs == "C": # scissors
                new_score += 2

        if match_decision == "Y":  # tie
            if theirs == "A":
                new_score += 1
            elif theirs == "B":
                new_score += 2
            elif theirs == "C":
                new_score += 3

        if match_decision == "Z":  # win
            if theirs == "A": # rock
                new_score += 2
            elif theirs == "B":  # paper
                new_score += 3
            elif theirs == "C": # scissors
                new_score += 1










    print(new_score)
    '''
    # OLD
    # calculate the score from you 
    yours = comp[1] # yours is the second one 
    score = score + int(scores[yours])

    addition = 0

    theirs = comp[0]
    # equal
    if theirs == yours_to_theirs[yours]:
        addition = 3

    # you have rock and they have paper
    elif theirs == "B" and yours == "X": # losing 
        addition = 0

    # you have rock they have scissors
    elif theirs == "C" and yours == "X":
        addition = 6

    # if you have scissors and they have rock
    elif theirs == "A" and yours == "Z": 
        addition = 0

    # if you have scissors and they have paper
    elif theirs == "B" and yours == "Z":  
        addition = 6

    # if you have paper and they have rock
    elif theirs == "A" and yours == "Y":  
        addition = 6

    # if you have paper and they have scissors
    elif theirs == "C" and yours == "Y":  
        addition = 0


    print("yours " + yours + " theirs " + theirs + " addition " + str(addition))
    score += addition
    '''