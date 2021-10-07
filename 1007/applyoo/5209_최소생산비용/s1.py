import sys
sys.stdin = open('input.txt')


def dfs(idx, c):
    global res
    if c >= res:
        return

    if idx == N:
        res = c
        return

    for i in range(N):
        if v[i]:
            v[i] = 0
            dfs(idx+1, c+A[idx][i])
            v[i] = 1


ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    res = 1500
    v = [1] * N
    dfs(0, 0)
    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')
