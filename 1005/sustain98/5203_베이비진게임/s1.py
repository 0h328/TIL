import sys
sys.stdin = open('input.txt')


def check(player_num):
    c = 0
    for i in players[player_num]:
        if i > 0:
            c += 1
            if c >= 3 or i >= 3:
                return 1
        elif c != 0:
            c = 0
    return 0


t = int(input())
for idx in range(1, t+1):
    l = list(map(int, input().split()))
    players = [[0]*10, [0]*10]
    res = 0
    for i in range(6):
        players[0][l[i*2]] += 1
        if check(0):
            res = 1
            break
        players[1][l[i*2 + 1]] += 1
        if check(1):
            res = 2
            break
    print('#{} {}'.format(idx, res % 3))