import sys
sys.stdin = open('input.txt')


def dfs(idx, p):
    global res
    if p <= res: return

    if idx == N:
        res = p
        return

    for i in range(N):
        if v[i]:
            v[i] = 0
            dfs(idx+1, p*A[idx][i]/100)
            v[i] = 1


ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    res = 0
    v = [1] * N
    dfs(0, 1)
    ans.append('#{0} {1:.6f}'.format(tc, 100*res))

print(*ans, sep='\n')