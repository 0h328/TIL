import sys
sys.stdin = open('input.txt')


def dfs(idx, rec):
    if rec == (1<<N) - 1: return 0
    if DP[idx][rec] != INF: return DP[idx][rec]

    c = INF
    for i in range(N):
        if A[idx][i] and not (rec&(1<<i)):
            c = min(c, A[idx][i] + dfs(idx+1, rec|(1<<i)))
    DP[idx][rec] = c
    return c


ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    INF = 1500
    DP = [[INF]*(1<<N) for _ in range(N)]
    ans.append('#{0} {1}'.format(tc, dfs(0, 0)))

print(*ans, sep='\n')