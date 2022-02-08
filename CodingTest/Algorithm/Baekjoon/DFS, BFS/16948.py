import sys
from collections import deque
sys.stdin = open('input.txt')

dr = [-2, -2, 0, 2, 2, 0]
dc = [-1, 1, -2, -1, 1, 2]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    v[x][y] = 1

    while q:
        r, c = q.popleft()

        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not v[nr][nc]:
                v[nr][nc] = v[r][c] + 1     # 갈수 있는 곳을 현재 위치에서 +1
                q.append((nr, nc))


N = int(input())
r1, c1, r2, c2 = map(int, input().split())
v = [[0] * N for _ in range(N)]

bfs(r1, c1)
print(v)
print(v[r2][c2]-1)
