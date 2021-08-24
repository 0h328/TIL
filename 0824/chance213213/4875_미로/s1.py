import sys
sys.stdin = open('input.txt')



def solve(arr, N, rowm, colm):
    global visited

    for k in range(3):
        ni = rowm + di[k]
        nj = colm + dj[k]
        visited[rowm][colm] = 1

        if arr[rowm][colm] == 2:
            ans = 1
            return ans
        elif -1 < ni < N and -1 < nj < N and arr[ni][nj] == 0 and visited[rowm][colm] == 0:
            rowm = ni
            colm = nj

            return solve(arr, N, rowm, colm)
        else:
            visited[rowm][colm] = -1
            ni -= di[k]
            nj -= dj[k]


T = int(input())
di = [0, 0, 1] #좌, 우, 아래
dj = [-1, 1, 0]
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]


    for idx in range(N):
        if arr[0][idx] == 3:
            start = idx
    for idx in range(N):
        if arr[N-1][idx] == 2:
            end = idx

    rowm = 0
    colm = start
    visited = [[0] * N for _ in range(N)]
    print(solve(arr, N, rowm, colm))