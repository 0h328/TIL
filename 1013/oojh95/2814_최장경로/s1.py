import sys
sys.stdin = open('input.txt')


def dfs(n, length):
    global result
    if length > result:
        result = length
    visited[n] = 1
    for i in range(N+1):
        if arr[n][i] == 1 and not visited[i]:
            dfs(i, length+1)

    visited[n] = 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    visited = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1
    result = 0
    for k in range(1, N+1):
        dfs(k, 1)
    print('#{} {}'.format(tc, result))