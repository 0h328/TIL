import sys

sys.stdin = open('input.txt')

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(r):
    r += 1
    if r >= 4:
        r -= 4
    return r


for idx in range(1, T + 1):
    n = int(input())
    snail = [[0] * n for _ in range(n)]

    r = 0
    x = 0
    y = 0
    tmp = 1
    snail[0][0] = 1
    while tmp < n * n:
        nx = x + dx[r]
        ny = y + dy[r]
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            r = turn(r)
            continue

        if snail[nx][ny] != 0:
            r = turn(r)
            continue

        tmp += 1
        snail[nx][ny] = tmp
        x = nx
        y = ny

    print('#{}'.format(idx))
    for i in range(n):
        print(' '.join(map(str, snail[i])))
