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

# from collections import deque
#
# # 4방 탐색
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]
#
# def bfs(x, y):
#
#     q = deque()
#     q.append((x, y))                        # 출발 위치 큐에 저장
#
#     while q:
#         r, c = q.popleft()                  # 출발 위치 꺼내서 탐색
#
#         for i in range(4):
#             nr = r + dr[i]
#             nc = c + dc[i]
#
#             if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1:    # 배열 범위 안, 1인 곳만 이동
#                 q.append((nr, nc))          # 다음 위치 큐에 저장
#                 arr[nr][nc] += arr[r][c]    # 이동한 곳을 누적합
#
# N, M = map(int, input().split())
# arr = []
# for _ in range(N):
#     arr.append(list(map(int, input())))
#
# bfs(0, 0)                                                           # 0, 0 시작
# print(arr[-1][-1])