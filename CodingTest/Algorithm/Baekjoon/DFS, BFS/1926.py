from collections import deque
import sys
sys.stdin = open('input.txt')

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(x, y, area):
    global max_area
    q = deque()
    q.append((x, y))
    v[x][y] = 1         # 방문한 곳에 대해 방문 체크

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if arr[nr][nc] == 1 and not v[nr][nc]:
                    v[nr][nc] = 1
                    area += 1
                    q.append((nr, nc))

    max_area = max(max_area, area)  # 그림을 돌때마다 영역 최댓값을 갱신

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
v = [[0] * m for _ in range(n)]

picture_cnt = 0
max_area = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1 and not v[i][j]:  # 방문체크 안하면 1인곳 다시 방문
            bfs(i, j, 1)                    # 방문과 동시에 area(영역) 체크
            picture_cnt += 1                # 다돌고 나오면 그림 +1

print(picture_cnt)
print(max_area)

