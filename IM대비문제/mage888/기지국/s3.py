import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    data = [list(input()) for _ in range(n)]

    acoor = []
    bcoor = []
    ccoor = []

    for i in range(n):
        for j in range(n):
            if data[i][j] == 'A':
                acoor.append((i, j))
            elif data[i][j] == 'B':
                bcoor.append((i, j))
            elif data[i][j] == 'C':
                ccoor.append((i, j))

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    if acoor:
        for i in range(len(acoor)):
            for k in range(1, 2):
                for j in range(4):
                    nr = acoor[i][0] + dr[j]*k
                    nc = acoor[i][1] + dc[j]*k
                    if nr in range(n) and nc in range(n):
                        data[nr][nc] = 'X'

    if bcoor:
        for i in range(len(bcoor)):
            for k in range(1, 3):
                for j in range(4):
                    nr = bcoor[i][0] + dr[j]*k
                    nc = bcoor[i][1] + dc[j]*k
                    if nr in range(n) and nc in range(n):
                        data[nr][nc] = 'X'

    if ccoor:
        for i in range(len(ccoor)):
            for k in range(1, 4):
                for j in range(4):
                    nr = ccoor[i][0] + dr[j]*k
                    nc = ccoor[i][1] + dc[j]*k
                    if nr in range(n) and nc in range(n):
                        data[nr][nc] = 'X'

    cnt = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == 'H':
                cnt += 1

    print('#{} {}'.format(tc, cnt))