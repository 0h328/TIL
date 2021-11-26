def dfs(r, c):
    global ans
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            if mazeArray[nr][nc] == 3:
                ans = 1
                return
            if not mazeArray[nr][nc] and not visited[nr][nc]:
                visited[nr][nc] = 1
                dfs(nr, nc)

import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    mazeArray = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    ans = 0
    x = 0
    y = 0
    for r in range(N):
        for c in range(N):
            if mazeArray[r][c] == 2:
                x, y = r, c
    dfs(x, y)
    print(ans)