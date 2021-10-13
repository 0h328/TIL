import sys
sys.stdin = open('input.txt')

def dfs(i, j):
    global ans
    for k in range(4):
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            if road[ni][nj] == 3:
                ans = 1
                return
            if not road[ni][nj] and not visited[ni][nj]:
                visited[ni][nj] = 1
                dfs(ni, nj)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    road = [list(map(int, list(input()))) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    ans = 0
    for i in range(N):
        for j in range(N):
            if road[i][j] == 2:
                dfs(i, j)
    print('#{} {}'.format(tc, ans))


##i, j 쓰지말자,, 오타발견도 못하고오오오오옹