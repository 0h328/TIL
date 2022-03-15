import sys
sys.stdin = open('input.txt')
from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    v = [[0] * C for _ in range(R)] # bfs 한번 돌때마다 v를 초기화 시켜야하므로 이 위치에 둬야함
    v[x][y] = 1
    tmp = 0

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < R and 0 <= nc < C:
                if arr[nr][nc] == 'L' and not v[nr][nc]:
                    v[nr][nc] = v[r][c] + 1
                    tmp = max(tmp, v[nr][nc])
                    q.append((nr, nc))

    return tmp-1

R, C = map(int, sys.stdin.readline().split())
arr = [sys.stdin.readline() for _ in range(R)]
cnt = 0

for i in range(R):
    for j in range(C):
        if arr[i][j] == 'L':
            cnt = max(cnt, bfs(i, j))   # 0,1 / 0,2 / 1,0 / .. 위치에서 출발해서 최대 거리 구하기

print(cnt)
