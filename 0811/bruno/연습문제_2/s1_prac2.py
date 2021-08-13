import sys
sys.stdin = open('input.txt')

N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
r = 1
c = 1

for i in range(4):
    nr = r + dr[i]
    nc = c + dc[i]

    #1. 벽 안으로 들어오는 경우만 수행
    if (0 <= nr < N) and (0 <= nc < N):
        print(data[nr][nc])

    #2. 벽 밖으로 나가면 그냥 continue
    if nr < 0 or nc >= N or nc < 0 or nc >= N:
        continue
