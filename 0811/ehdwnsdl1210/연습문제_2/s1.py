import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

print(DataFrame(L))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
# 상하좌우

r, c = 1, 1

for i in range(4):

    nr = r + dr[i]
    nc = c + dc[i]

    #1. 벽 안으로 들어오는 경우만 수행
    if (-1 < nr < N) and (-1 < nc < N):
        print(L[nr][nc])

    #2. q벽 밖으로 나가면 그냥 continue
    if nr < 0 or nr >= N or nc < 0 or nc >= N:
        continue


drc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for r, c in drc:
    print(r, c)