import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    for j in range(len(dp[i])):
        if i == j:
            dp[i][j] += dp[i-1][j-1]
        elif j == 0:
            dp[i][j] += dp[i-1][j]
        else:
            dp[i][j] += max(dp[i-1][j], dp[i-1][j-1])


print(max(dp[n-1]))