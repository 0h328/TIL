# DFS
# import sys
# sys.stdin = open('input.txt')
# sys.setrecursionlimit(10**6)
#
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
#
# def dfs(r, c):
#     global v_cnt, k_cnt
#     v[r][c] = 1
#
#     if arr[r][c] == 'v':      # 방문한 곳이 늑대면
#         v_cnt += 1            # 늑대의 수  +1
#     elif arr[r][c] == 'k':    # 방문한 곳이 양이면
#         k_cnt += 1            # 양의 수 +1
#
#     for i in range(4):
#         nr = r + dr[i]
#         nc = c + dc[i]
#
#         if 0 <= nr < R and 0 <= nc < C:
#             if arr[nr][nc] != '#' and not v[nr][nc]:
#                 v[nr][nc] = 1
#                 dfs(nr, nc)
#
# R, C = map(int, sys.stdin.readline().split())
# arr = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
# v = [[0] * C for _ in range(R)]
#
# sheep = 0
# wolf = 0
#
# for i in range(R):
#     for j in range(C):
#         v_cnt = 0
#         k_cnt = 0
#         if arr[i][j] != '#' and not v[i][j]:  # '#'은 울타리
#             dfs(i, j)
#             if v_cnt >= k_cnt:    # 늑대가 양보다 많거나 같으면
#                 wolf += v_cnt     # 늑대의 수를 누적하고
#                 k_cnt = 0         # 양은 모두 0
#             else:                 # 그 반대면
#                 sheep += k_cnt    # 양의 수를 누적하고
#                 v_cnt = 0         # 늑대는 모두 0
#
# print(sheep, wolf)

# BFS
from collections import deque
import sys
sys.stdin = open('input.txt')

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def bfs(x, y):
    global v_cnt, k_cnt
    v[x][y] = 1
    q = deque()
    q.append((x, y))

    while q:
        r, c = q.popleft()

        if arr[r][c] == 'v':    # 방문한 곳이 늑대면
            v_cnt += 1          # 늑대의 수  +1
        elif arr[r][c] == 'k':  # 방문한 곳이 양이면
            k_cnt += 1          # 양의 수 +1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < R and 0 <= nc < C:
                if arr[nr][nc] != '#' and not v[nr][nc]:
                    v[nr][nc] = 1
                    q.append((nr, nc))


R, C = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
v = [[0] * C for _ in range(R)]

sheep = 0
wolf = 0

for i in range(R):
    for j in range(C):
        v_cnt = 0
        k_cnt = 0
        if arr[i][j] != '#' and not v[i][j]:    # '#'은 울타리
            bfs(i, j)
            if v_cnt >= k_cnt:  # 늑대가 양보다 많거나 같으면
                wolf += v_cnt   # 늑대의 수를 누적하고
                k_cnt = 0       # 양은 모두 0
            else:               # 그 반대면
                sheep += k_cnt  # 양의 수를 누적하고
                v_cnt = 0       # 늑대는 모두 0

print(sheep, wolf)
