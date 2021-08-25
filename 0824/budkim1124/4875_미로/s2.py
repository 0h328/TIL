def dfs(start_i, start_j):
    global result

    if arr[start_i][start_j] == 3:
        result = 1
        return

    for k in range(4):
        nx, ny = start_i + dx[k], start_j + dy[k]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1 and (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs(nx, ny)
            # visited.remove((nx, ny))

import sys
sys.stdin = open("input.txt")

T = int(input())

for t in range(T):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = []


    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start_i, start_j = i, j


    result = 0
    dfs(start_i, start_j)
    print("#{} {}".format(t+1, result))