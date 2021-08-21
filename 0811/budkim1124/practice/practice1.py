import sys
sys.stdin = open('input.txt')
from pandas import DataFrame

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

r = 1
c = 1

#drc = [[-1,0], [1,0], [0,-1], [0,1]]
#
# for r, c in  drc:
#     print(r,c)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(4):
    # print(dr[i], dc[i])

    nr = r + dr[i] # r로부터 dr만큼 이동한 새로운 nr
    nc = c + dc[i]

    #1. 벽 안으로 들어오는 경우만 수행
    if (0 <= nr < N) and (0 <= nc <N):
        print(data[nr][nc])

    #2. 벽 밖으로 나가면 그냥 continue
    if nr < 0 or nr >= N or nc < 0 or nc >= N:
        continue
