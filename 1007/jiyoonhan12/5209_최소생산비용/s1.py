import sys
sys.stdin = open('input.txt')


def dfs(i, total):
    global ans

    if i == N:
        if total < ans:
            ans = total
        return

    if total >= ans:
        return

    for k in range(N):
        if not visited[k]:
            visited[k] = 1
            dfs(i+1, total + arr[i][k])
            visited[k] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 1500

    dfs(0, 0)
    print('#{} {}'.format(t, ans))