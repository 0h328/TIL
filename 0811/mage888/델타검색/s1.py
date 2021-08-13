import sys
sys.stdin = open('input.txt')

M = 3
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
#
# for i in range(N):
#     for j in range(M):
#         for k in range(3):
#             ni = i + di[k]
#             nj = j + dj[k]
#             if 0 <= ni < N and 0 <= nj < M:
#                 print(A[ni][nj], end= ' ')

di = [0] * (N + 1) # [0, 0, 0, 0]
dj = [0] * (M + 1) # [0, 0, 0, 0]

# 현재 위치 지정하는 법?

for i in range(N):
    for j in range(M):
        if abs(i-j) == 1:
            if j == 1:
                print(A[i][j])

for i in range(N):
    for j in range(M):
        if abs(i-j) == 1:
            if i == 1:
                print(A[i][j])







