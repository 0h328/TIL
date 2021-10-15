import sys
from collections import deque
sys.stdin = open('input.txt')

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def bfs(x, y):
    v[x][y] = 0
    q = deque()
    q.append((x, y))

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if v[nr][nc] > arr[nr][nc] + v[r][c]:
                    v[nr][nc] = arr[nr][nc] + v[r][c]
                    q.append((nr, nc))
    return

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    v = [[float('INF') for _ in range(N)] for _ in range(N)]
    bfs(0, 0)

    print('#{} {}'.format(tc, v[-1][-1]))