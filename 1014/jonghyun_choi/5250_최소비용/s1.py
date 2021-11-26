import sys
sys.stdin = open('input.txt')

from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[987654321] * N for _ in range(N)]
    q = deque()
    q.append((0, 0))
    visited[0][0] = 0
    while q:
        r, c = q.popleft()

        for k in range(4):
            next_r = r + dr[k]
            next_c = c + dc[k]
            if 0 <= next_r < N and 0 <= next_c < N:
                fuel = data[next_r][next_c] - data[r][c]
                if fuel <= 0:
                    fuel = 0
                if visited[next_r][next_c] > visited[r][c] + fuel + 1:
                    visited[next_r][next_c] = fuel + 1 + visited[r][c]
                    q.append((next_r, next_c))

    print('#{} {}'.format(case + 1, visited[N - 1][N - 1]))

