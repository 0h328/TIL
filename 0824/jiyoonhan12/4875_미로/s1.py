import sys
sys.stdin = open('input.txt')


def solve(si, sj):
    global res

    if arr[si][sj] == 3:
        res = 1
        return

    visited.append((si, sj))
    for k in range(4):
        ni = si + di[k]
        nj = sj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != 1 and (ni, nj) not in visited:
            solve(ni, nj)

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    si, sj = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                si = i
                sj = j

    # 위 오른 아래 왼
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    res = 0
    visited = []
    solve(si, sj)
    print('#{} {}'.format(t, res))