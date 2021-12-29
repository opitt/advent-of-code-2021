# pos = [4, 8] # test
pos = [1, 10] # start values
dice = [6, 15] # start values
score = [0, 0] # start values
DICE_INC = 18
winner = None
rolls = 0

while True:
    for p in (0, 1):
        rolls += 3

        pos[p] = (pos[p] + dice[p]) % 10 or 10
        dice[p] = (dice[p] + 18) % 100 or 10

        score[p] += pos[p]
        if score[p] >= 1000:
            winner = p
            looser = 0 if winner==1 else 1
            break
    if winner != None:
        break

print(f"{rolls=}*{score[looser]=} = {rolls*score[looser]} ") # part 1: 428736
