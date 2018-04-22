import random

val = ['r', 'p', 's']

def valid(ans):
    if ans not in val:
        return False
    else:
        return True

def play(_u,_c):

    win = {'r':'s','p':'r','s':'p'}
    if _u == _c:
        return 'again'
    elif win[_u] == _c:
        return 'Won'
    else:
        return 'Lost'

def c():
    _rand = random.randint(0, 2)
    _c = val[_rand]
    return _c

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


