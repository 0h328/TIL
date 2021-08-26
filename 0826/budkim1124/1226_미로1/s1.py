def dfs(start_i, start_j):
    global result

    if arr[start_i][start_j] == '3':
        result = 1
        return
    # visited.append((start_i, start_j))
    for k in range(4):
        nx, ny = start_i + dx[k], start_j + dy[k]
        if 0 <= nx < 16 and 0 <= ny < 16 and arr[nx][ny] != '1' and (nx, ny) not in visited:
            visited.append((nx, ny))
            dfs(nx, ny)
            # visited.remove((nx, ny))

import sys
sys.stdin = open("input.txt")

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(10):
    N = int(input())
    arr = [list(input()) for _ in range(16)]
    # print(arr)
    visited = []

    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                start_i, start_j = i, j

    result = 0
    dfs(start_i, start_j)
    print("#{} {}".format(N, result))