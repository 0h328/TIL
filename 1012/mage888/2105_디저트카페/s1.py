import sys
sys.stdin = open('input.txt')

dr = [1, 1, -1, -1]
dc = [1, -1, 1, -1]

def route(r, c, start_r, start_c, d):
    global cnt

    if d == 4:
        return

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not v[cafe[nr][nc]]:
            pass

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cafe = [list(map(int, input().split())) for _ in range(N)]
    v = [0]*101
    max_num = -1
    cnt = 1

    for i in range(1, N-1):
        for j in range(N):
            v[cafe[i][j]] = 1
            route(i+1, j+1, i, j, 0)
            v[cafe[i][j]] = 0





