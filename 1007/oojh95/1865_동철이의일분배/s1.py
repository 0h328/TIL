import sys
sys.stdin = open('input.txt')


def dfs(n, p):
    global result

    if n == N:
        if p > result:
            result = p
        return
    if p <= result:
        return
    for i in range(N):
        if P[n][i] != 0 and not visited[i]:
            visited[i] = 1
            dfs(n+1, p*P[n][i]/100)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    visited = [0] * N
    p = 1.0
    dfs(0, 1.0)
    result *= 100
    print('#{} {:.6f}'.format(tc, result))
