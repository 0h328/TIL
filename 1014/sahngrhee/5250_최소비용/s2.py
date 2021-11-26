import sys
sys.stdin = open('input.txt')
from collections import deque


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    while queue:
        x, y = queue.popleft()
        if not visited[x][y]:
            visited[x][y] = 1
        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny]:
                    queue.append((nx, ny))
                    if H[x][y] >= H[nx][ny]:
                        fuel[nx][ny] = fuel[x][y] + 1
                    else:
                        fuel[nx][ny] = fuel[x][y] + 1 + H[nx][ny] - H[x][y]


T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    fuel = [[0] * N for _ in range(N)]
    bfs(0, 0)
    print('#{} {}'.format(test_case, fuel[N-1][N-1]-1))