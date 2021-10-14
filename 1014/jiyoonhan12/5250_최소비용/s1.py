import sys
sys.stdin = open('input.txt')

# dfs 시간초과

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(r, c, temp):
    global ans, visited
    if temp >= ans:
        return
    if r == N-1 and c == N-1:
        if temp < ans:
            ans = temp
        return
    for k in range(4):
        ni = r + di[k]
        nj = c + dj[k]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            visited[ni][nj] = 1
            if arr[ni][nj] > arr[r][c]:
                dfs(ni, nj, temp + 1 + arr[ni][nj] - arr[r][c])
            else:
                dfs(ni, nj, temp + 1)
            visited[ni][nj] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    ans = 987654321
    visited[0][0] = 1
    dfs(0, 0, 0)
    print('#{} {}'.format(t, ans))