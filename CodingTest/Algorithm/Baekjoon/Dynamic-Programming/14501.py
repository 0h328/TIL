import sys
sys.stdin = open('input.txt')

N = int(input())
case = []
dp = [0] * (N+1)
check = 0

for _ in range(N):
    t, p = map(int, input().split())
    case.append([t, p])

for i in range(N):
    check = max(check, dp[i])
    if case[i][0] + i <= N :
        dp[case[i][0] + i] = max(case[i][1]+check, dp[case[i][0] + i])

print(max(dp))
