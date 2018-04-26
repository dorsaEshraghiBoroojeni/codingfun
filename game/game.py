import random


#accepted input values (user choice)
val = ['r', 'p', 's']
#validate user input
def valid(ans):
    if ans not in val:
        return False
    else:
        return True

# _u stands for you and _c stands for computer choice
def play(_u,_c):


    if _u == _c:
        return 'again'
    elif win[_u] == _c:
        return 'Won'
    else:
        return 'Lost'
#comuter choice is a random value between 0 - 1 -2
def c():
    _rand = random.randint(0, 2)
    _c = val[_rand]
    return _c
#continue the game until someone wins
if __name__ == "__main__":
    res = 'again'
    while res == 'again':
        _u = input("choose Rock, Paper or Scissors by typing the letter ‘r’, ‘p’ or ‘s’ or exit\n")
        if _u == "exit":
            break
        if not valid(_u):
            continue
        _c = c()
        res = play(_u , _c)
        print (res,"\nMy choice was : %c " %_c)


