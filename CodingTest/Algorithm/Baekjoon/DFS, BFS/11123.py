from collections import deque
import sys
sys.stdin = open('input.txt')

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    v[x][y] = 1

    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < H and 0 <= nc < W:
                if arr[nr][nc] == '#' and not v[nr][nc]:
                    v[nr][nc] = 1
                    q.append((nr, nc))

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    arr = [list(input()) for _ in range(H)]
    v = [[0] * W for _ in range(H)] # 영역의 개수를 셀때는 방문체크
    cnt = 0

    for i in range(H):
        for j in range(W):
            if arr[i][j] == '#' and not v[i][j]:
                bfs(i, j)
                cnt += 1

    print(cnt)