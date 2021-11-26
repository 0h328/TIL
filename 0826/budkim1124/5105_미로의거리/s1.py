def bfs(start_i, start_j):
    global result
    Q = []
    Q.append((start_i, start_j))

    while Q:
        x, y = Q.pop(0)
        visited[x][y] = 1
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] != '1':
                Q.append((nx, ny))
                c_list[nx][ny] = c_list[x][y] + 1
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] == '3':
                    c_list[nx][ny] = c_list[x][y]
                    result = c_list[nx][ny]
                    return


import sys
sys.stdin = open("input.txt")

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    c_list = [[0]*(N) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                start_i, start_j = i, j

    result = 0
    bfs(start_i, start_j)
    print("#{} {}".format(t+1, result))
