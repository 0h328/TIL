import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
cases = [int(input()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1

for case in cases:  # 1,2,5
    for i in range(case, k+1):  # 각각의 금액~목표 금액까지 범위 설정
        dp[i] += dp[i-case]     # ex) 5원의 경우에는 4원이 될 수 없으므로
                                # 1원으로 1원~10원 만드는 경우의 수 누적
print(dp[-1])                   # 2원으로 2원~10원 만드는 경우의 수 누적
                                # 5원으로 5월~10원 만드는 경우의 수 누적