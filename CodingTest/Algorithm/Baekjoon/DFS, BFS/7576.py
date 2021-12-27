# 최단거리, 최단시간은 무조건 BFS
from collections import deque
import sys
sys.stdin = open('input.txt')

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

q = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j))    # 1(익은 토마토)의 좌표를 모두 q에 넣는다.

while q:
    (r, c) = q.popleft()    # 익은 토마토 꺼내서

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:    # 인접한 위치의 안익은 토마토를 찾고
            q.append((nr, nc))                                  # 해당 토마토를 익히고 좌표를 q에 넣어준다.
            arr[nr][nc] = arr[r][c] + 1                         # 익혔으니 날짜 수를 더해준다.

min_day = 0 # 토마토가 모두 익을때까지 걸린 날
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:  # 빈 곳은 -1, 익힌 곳은 더한 날짜(1이상)로 채워지고, 0이면 창고에 모든 토마토가 익지 않음
            print(-1)       # 모두 익지 못했으니 -1을 출력
            exit()          # 강제 종료
    if min_day < max(arr[i]):   # 익을때까지 걸린 날보다 작으면
        min_day = max(arr[i])   # 갱신해준다.

print(min_day-1)






