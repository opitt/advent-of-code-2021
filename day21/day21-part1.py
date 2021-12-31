DICE_INC = 18
MAX_POS = 10
MAX_DICE = 100
winner = looser = -1

# pos = [4, 8] # test positions
pos   = [1, 10] # start values
dice  = [6, 15] # start values
score = [0,  0] # start values
rolls = 0

while winner < 0:
    for p in (0, 1):
        rolls += 3 # three rolls
        pos[p] = (pos[p] + dice[p]) % MAX_POS or MAX_POS
        dice[p] = (dice[p] + DICE_INC) % 100 or MAX_DICE

        score[p] += pos[p]
        if score[p] >= 1000:
            winner = p
            looser = 0 if winner==1 else 1
            break

print(f"{rolls=}*{score[looser]=} = {rolls*score[looser]} ") # part 1: 428736
