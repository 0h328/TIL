# 미로탐색
from collections import deque

import sys
sys.stdin = open('input.txt')

def bfs(r, c):

    q = deque()
    v[r][c] = 1
    q.append((r, c))

    while q:
        (r, c) = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M and not v[nr][nc] and arr[nr][nc]:
                q.append((nr, nc))
                v[nr][nc] = v[r][c] + 1


N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
v = [[0 for _ in range(M)] for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

bfs(0, 0)
print(v[-1][-1])

# def dfs(r, c, cnt):
#     global max_cnt

#     v[r][c] = 1

#     if max_cnt <= cnt:
#         return

#     if r == N - 1 and c == M - 1:
#         if cnt < max_cnt:
#             max_cnt = cnt
#             return

#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]

#         if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] and not v[nr][nc]:
#             dfs(nr, nc, cnt+1)
#             v[nr][nc] = 0



# N, M = map(int, input().split())
# arr = [list(map(int, input())) for _ in range(N)]
# v = [[0 for _ in range(M)] for _ in range(N)]

# max_cnt = 10001

# dr = [1, 0, -1, 0]
# dc = [0, -1, 0, 1]

# dfs(0, 0, 1)
# print(max_cnt)