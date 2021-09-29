import sys
sys.stdin = open('input.txt')


def backtrack(i, j, cnt, tf):
    global max_length, g

    if cnt > max_length:
        max_length = cnt

    visited[i][j] = 1
    for m in range(4):
        ni, nj = i + dx[m], j + dy[m]
        if -1 < ni < n and -1 < nj < n and visited[ni][nj] == 0:
            if g[ni][nj] < g[i][j]:
                backtrack(ni, nj, cnt + 1, tf)
            elif (not tf) and (g[ni][nj] - k) < g[i][j]:
                original_val = g[ni][nj]
                g[ni][nj] = g[i][j] - 1
                backtrack(ni, nj, cnt + 1, True)
                g[ni][nj] = original_val

    visited[i][j] = 0



t = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for idx in range(1, t+1):
    n, k = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    max_height = max(map(max, g))

    max_length = 1
    for i in range(n):
        for j in range(n):
            if g[i][j] == max_height:
                backtrack(i, j, 1, False)

    print('#{} {}'.format(idx, max_length))
