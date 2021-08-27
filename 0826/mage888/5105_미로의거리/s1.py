import sys
sys.stdin = open('input.txt')

def dfs(start_r, start_c):
    global cnt, r, c
    r = start_r
    c = start_c

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    i = 0

    while data[r][c] != 3:
        nr = r + dr[i]
        nc = c + dc[i]

        if nr in range(N) and nc in range(N):
            if data[nr][nc] == 0 or data[nr][nc] == 3:
                r = nr
                c = nc
                cnt += 1
                data[nr][nc] = -1

        i = (i + 1) % 4

    return cnt
    pass

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]

    cnt = 0

    for r in range(N):
        for c in range(N):
            if data[r][c] == 2:
                break

    ans = dfs(r, c)

    # print('#{} {}'.format(tc, ans))