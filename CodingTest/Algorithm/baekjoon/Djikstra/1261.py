from collections import deque
import sys
sys.stdin = open('input.txt')
INF = 1000000

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(x, y):
    v[x][y] = 0
    q = deque()
    q.append((x, y))

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if v[nr][nc] > arr[nr][nc] + v[r][c]:
                    v[nr][nc] = arr[nr][nc] + v[r][c]
                    q.append((nr, nc))
    return

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
v = [[INF] * M for _ in range(N)]
bfs(0, 0)

print(v[-1][-1])