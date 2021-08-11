# 수업시간 풀이
import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    ans = [[0] * N for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    d = 0
    x = -1
    y = 0
    i = 1

    while True:
        nxt_x = x + dx[d]
        nxt_y = y + dy[d]

        if nxt_x >= N or nxt_y >= N or ans[nxt_y][nxt_x] != 0:
            d = (d+1) % 4
            continue

        x = nxt_x
        y = nxt_y
        ans[y][x] = i
        i += 1

        if i > N ** 2:
            break

    print('#{}'.format(tc))
    for lst in ans:
        print(' '.join(map(str, lst)))