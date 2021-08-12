import sys
sys.stdin = open('input.txt')

N = int(input())

L = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 상 하 좌 우

# for i in range(len(L)):
#     for j in range(len(L)):
#         for k in range(4):
#             ni = i + dx[k]
#             nj = j + dy[k]
#             if 0 <= ni < N and 0 <= nj < N:
#                 print(L[ni][nj], end= ' ')