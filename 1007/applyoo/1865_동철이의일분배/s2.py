import sys
sys.stdin = open('input.txt')


def dfs(idx, rec):
    if rec == (1<<N) - 1: return 1
    if DP[idx][rec]: return DP[idx][rec]

    p = 0
    for i in range(N):
        if A[idx][i] and not (rec&(1<<i)):
            p = max(p, A[idx][i]/100 * dfs(idx+1, rec|(1<<i)))
    DP[idx][rec] = p
    return p


ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    DP = [[0] * (1<<N) for _ in range(N)]
    ans.append('#{0} {1:.6f}'.format(tc, 100*dfs(0, 0)))
print(*ans, sep='\n')