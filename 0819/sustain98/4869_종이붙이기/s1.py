import sys
from collections import defaultdict
sys.stdin = open('input.txt')

# dp = defaultdict(int)
# dp[1] = 1
# dp[2] = 2
# idx = 0
# t = int(input())
# for num in range(1, t+1):
#     n = int(input())//10
#     for idx in range(idx+1, n):
#         dp[idx+1] += dp[idx]
#         dp[idx+2] += dp[idx]*2
#     print('#{} {}'.format(num, dp[n]))


dp = [0,1,3] + [0]*28
t = int(input())
idx = 2
for num in range(1, t+1):
    n = int(input())//10
    for idx in range(idx+1, n+1):
        dp[idx] = dp[idx-1] + dp[idx-2]*2
    print('#{} {}'.format(num, dp[n]))
