import sys
sys.stdin = open('input.txt')


ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    INF, m = 1500, (1<<N)
    DP = [0] + [INF] * (m-1)
    for i in range(m):
        t = bin(i).count('1')
        for j in range(N):
            if not (i&(1<<j)):
                DP[i|(1<<j)] = min(DP[i|(1<<j)], A[t][j] + DP[i])

    ans.append('#{0} {1}'.format(tc, DP[-1]))

print(*ans, sep='\n')
