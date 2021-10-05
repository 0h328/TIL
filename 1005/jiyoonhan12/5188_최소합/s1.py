import sys
sys.stdin = open('input.txt')

di = [0, 1]
dj = [1, 0]


def dfs(i, j, temp):
    global res

    if temp >= res:             # 중간에 경우 안 줄여주면 시간초과
        return

    if i == N-1 and j == N-1:
        if temp < res:
            res = temp

    for k in range(2):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            visited[ni][nj] = 1
            dfs(ni, nj, temp + arr[ni][nj])
            visited[ni][nj] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    res = 32500
    # start 0, 0 / end N-1, N-1
    dfs(0, 0, arr[0][0])
    print('#{} {}'.format(t, res))