import sys
sys.stdin = open('input.txt')

def dfs(r, c, dist):
    global ans
    if dist >= ans:
        return

    if r == N-1 and c == N-1:
        ans = min(ans, dist)
    else:
        if r + 1 < N:
            dfs(r+1, c, dist + arr[r+1][c])
        if c + 1 < N:
            dfs(r, c+1, dist + arr[r][c+1])

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = 987654321
    dfs(0, 0, arr[0][0])
    print('#{} {}'.format(tc, ans))
