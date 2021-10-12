import sys

sys.stdin = open('input.txt')

# 동완님 풀이
def dfs(idx, rec):
    if rec == END: return 1
    if DP[rec]:
        return DP[rec]

    p = 0
    for i in range(N):
        if not (rec & (1 << i)):
            p = max(p, A[idx][i] / 100 * dfs(idx + 1, rec | (1 << i)))
    DP[rec] = p
    return p


ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    END = (1 << N) - 1
    DP = [0] * (END + 1)
    ans.append('#{0} {1:.6f}'.format(tc, 100 * dfs(0, 0)))

print(*ans, sep='\n')