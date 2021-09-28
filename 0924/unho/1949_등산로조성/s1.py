import sys

sys.stdin = open('input.txt')


def dfs(i, j, k, ans):
    global answer

    for a in range(4):
        y = i + dr[a]
        x = j + dc[a]

        if 0 <= y < N and 0 <= x < N and not visited[y][x]:
            if mountain[i][j] > mountain[y][x]:
                visited[y][x] = True
                dfs(y, x, k, ans + 1)
                visited[y][x] = False
            elif k and mountain[i][j] > mountain[y][x] - k:
                restore = mountain[y][x]
                mountain[y][x] = mountain[i][j] - 1
                visited[y][x] = True
                dfs(y, x, 0, ans + 1)
                mountain[y][x] = restore
                visited[y][x] = False

    if answer < ans:
        answer = ans


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    answer = 0
    high = 0

    for i in range(N):
        tmp = max(mountain[i])
        if high < tmp:
            high = tmp

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == high:
                visited[i][j] = True
                dfs(i, j, K, 1)
                visited[i][j] = False

    print('#{} {}'.format(tc, answer))