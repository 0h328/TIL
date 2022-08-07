import sys
sys.stdin = open('input.txt')

def sol(x):

	if x == 1 or x == 2:
		return 1
	if x == 3 :
		return 2
	if dp[x] != 0 :
		return dp[x]
	dp[x] = sol(x-1) + sol(x-2)
	return dp[x]

N = int(input())
dp = [0] * (N+1)

print(sol(N))