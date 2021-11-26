import sys
sys.stdin = open('input.txt')

N = int(input())
nums = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)


if N == 1:
    print(nums[1])

else:
    dp[1] = nums[1]
    dp[2] = nums[1] + nums[2]
    for i in range(3, N+1):
        dp[i] = max(dp[i-3] + nums[i-1] + nums[i], dp[i-2] + nums[i])
    print(dp[N])

    # 규칙 찾기
    # dp[3] = dp[1] + nums[3], dp[0] + nums[2] + nums[3]
    # dp[4] = dp[2] + nums[4], dp[1] + nums[3] + nums[4]
    # dp[5] = dp[3] + nums[5], dp[2] + nums[4] + nums[5]