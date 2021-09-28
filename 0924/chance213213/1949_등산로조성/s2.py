import sys
sys.stdin = open('input.txt')
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

def calc(i, j, road, skill):
    global result
    if road > result:
        result = road

    visited[i][j] = 1
    for s in range(4):
        ni = i + di[s]
        nj = j + dj[s]
        if ni >= 0 and ni < N and nj >= 0 and nj < N:
            if maps[ni][nj] < maps[i][j]:
                calc(ni, nj, road+1, skill)
            elif skill==1 and (maps[ni][nj] - K) < maps[i][j]:
                tmp = maps[ni][nj]
                maps[ni][nj] = maps[i][j]-1
                calc(ni, nj, road+1, 0)
 #               skill = 0
 #               calc(ni, nj, road+1, skill)
                maps[ni][nj] = tmp
            visited[i][j] = 0

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    h_max = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] > h_max:
                h_max = maps[i][j]
    visited = [[0] * N for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N):
            if maps[i][j] == h_max:
                calc(i, j, 1, 1)

    print('#{} {}'.format(tc, result))