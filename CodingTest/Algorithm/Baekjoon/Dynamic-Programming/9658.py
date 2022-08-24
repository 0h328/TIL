import sys
sys.stdin = open('input.txt')

N = int(input())

dp = [False] * 1001
dp[2] = True

for i in range(4, N+1):
  if not dp[i-1]:
    dp[i] = True
  if not dp[i-3]:
    dp[i] = True
  if not dp[i-4]:
    dp[i] = True

print('SK' if dp[N] else 'CY')