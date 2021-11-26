import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    dp = [0] * 101
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for i in range(4, N+1):
        dp[i] = dp[i-3] + dp[i-2]

    print(dp[N])