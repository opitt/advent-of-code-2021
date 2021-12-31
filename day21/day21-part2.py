from functools import lru_cache

MAX_POS = 10
WIN = 21
#start_pos = (4, 8)  # test positions
start_pos = (1, 10)  # start values
score = (0, 0)  # start values


def calc_pos(pos, dice):
    return (pos + dice) % MAX_POS or MAX_POS

@lru_cache(maxsize=None)
def next_roll(cur_pos, cur_score, cur_player):
    # we roll the dice for current player and see, which dice rolls let her win. 
    # If she does not win, we roll the dice for the next player.
    # while we store, how many times each player won

    # convert tuple back to list (lru cache requires immutable values!)   
    cur_pos = list(cur_pos)
    cur_score = list(cur_score)

    # dice3: we roll 3x the dice. the result can be 1-1-1 or 2-1-1 or 1-2-1 etc. this means the
    # sum of the three dices can be between 3 and 9 ... but different many times (frequency).
    # 3 can only be achieved by rolling 1+1+1 and 9 by 3+3+3 but 4 can be rolled in 3 different ways ...
    dice3 = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

    next_player = 1 if cur_player == 0 else 0
    wins_in_this_round = [0, 0]
    
    #now we test all possible dice sum outcomes
    for val, frequ in dice3.items():
        pos = calc_pos(cur_pos[cur_player], val)
        score = cur_score[cur_player] + pos
        if score >= WIN:
            wins_in_this_round[cur_player] += frequ
        else:
            next_pos = cur_pos[:]
            next_pos[cur_player] = pos
            next_score = cur_score[:]
            next_score[cur_player] = score
            next_wins = next_roll(tuple(next_pos), tuple(next_score), next_player)
            # the next step is important
            # since the other player plays  in frequ - universes, we need to multiply the wins
            wins_in_this_round[0] += next_wins[0] * frequ
            wins_in_this_round[1] += next_wins[1] * frequ
    return wins

# need to use tuple instead of list, due to the lru_cache decorator
wins = next_roll(start_pos, score, 0)
print(f"Player 0 with {wins[0]}" if wins[0]>wins[1] else "Player 1 with {wins[1]}")
