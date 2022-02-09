import sys
from collections import deque
sys.stdin = open('input.txt')

dr = [1, 0, -1, 0, 1, -1, 1, -1]
dc = [0, 1, 0, -1, -1, 1, 1, -1]
def bfs(x, y):
    q = deque()
    q.append((x, y))
    v[x][y] = 1

    while q:
        r, c = q.popleft()

        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < M and 0 <= nc < N:
                if arr[nr][nc] == 1 and not v[nr][nc]:
                    v[nr][nc] = 1
                    q.append((nr, nc))


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
v = [[0] * N for _ in range(M)]
cnt = 0

for i in range(M):
    for j in range(N):
        if arr[i][j] == 1 and not v[i][j]:
            bfs(i, j)
            cnt += 1    # 1로 연결된 곳만 세면 되므로 bfs 끝나고 +1

print(cnt)