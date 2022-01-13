# DFS
import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    arr[r][c] = -1  # 0인 곳은 모두 -1로 바꿔줌
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < M and 0 <= nc < N:
            if not arr[nr][nc]:
                dfs(nr, nc)

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(M)]

for j in range(N):
    if not arr[0][j]:
        dfs(0, j)

if arr[M-1].count(-1):  # 행의 마지막 배열에 -1이 존재하면 YES
    print('YES')
else:
    print('NO')

# BFS
# from collections import deque
# import sys
# sys.stdin = open('input.txt')
#
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
#
# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#     v[x][y] = 1
#
#     while q:
#         r, c = q.popleft()
#         if r == M-1:        # 행이 마지막 인덱스에 도착하면 성공
#             print('YES')
#             exit()
#
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#
#             if 0 <= nr < M and 0 <= nc < N:
#                 if not arr[nr][nc] and not v[nr][nc]:
#                     v[nr][nc] = 1
#                     q.append((nr, nc))
#
#
# M, N = map(int, sys.stdin.readline().split())
# arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(M)]
# v = [[0] * N for _ in range(M)]
#
# for j in range(N):
#     if not arr[0][j] and not v[0][j]:
#         bfs(0, j)
#
# print('NO')
