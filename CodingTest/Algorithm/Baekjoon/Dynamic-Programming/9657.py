import sys
sys.stdin = open('input.txt')

N = int(input())
dp = [0, 'Win', 'Lose', 'Win', 'Win'] + [0]*(N-4)

if N <= 4:
    pass
else:
    for i in range(5, N+1):
        if 'Lose' in [dp[i-1], dp[i-3], dp[i-4]]:
            dp[i] = 'Win'
        else:
            dp[i] = 'Lose'

if dp[N] == 'Win':
    print('SK')
else:
    print('CY')