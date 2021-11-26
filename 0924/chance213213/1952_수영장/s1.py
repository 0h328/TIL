import sys
sys.stdin = open('input.txt')

#cost : 이전 달까지 계산 한 거, m은 현내 내가 보낼 결과임
def calc(cost, m):
    global min_cost
    if m > 12: #베이스 캠프,
        if min_cost < cost:
            min_cost = cost
        return
    #1일권
    calc(cost + d * month[m], m+1) #다음 달로 넘기기
    calc(cost + m1, m+1)
    calc(cost + m3, m+3)


T = int(input())
for tc in range(1, T+1):
    d, m1, m3, y = map(int, input(). split())

    month = [0] + list(map(int, input().split()))
    min_cost = y

    dp = [0] * 13
    dp[1] = min(m1, month[1] * d)
    dp[2] = dp[1] + min(m1, month[2]*d)

    for i in range(3, 13):
        dp[i] = min(dp[i-3] + m3, dp[i-1]+m1, dp[i-1] + month[i]*d)

    print()