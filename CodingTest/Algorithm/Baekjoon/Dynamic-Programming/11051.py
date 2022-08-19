import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(N+1):
        if j == 0:
            dp[i][j] = 1
        elif i == j:
            dp[i][j] = 1
        elif j == 1:
            dp[i][j] = i
        elif N >= K:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]


print(dp[N][K] % 10007)