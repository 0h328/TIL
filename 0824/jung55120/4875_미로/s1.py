def find_miro(r, c):
    for i in range(4):
        nx = r + dx[i]
        ny = c + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if miro[nx][ny] == 3:
                return 1
            if not miro[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                find_miro(nr, nc)

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    miro = [list(map(int, input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                x, y = i, j
                find_miro(x, y)

    print(find_miro(point))