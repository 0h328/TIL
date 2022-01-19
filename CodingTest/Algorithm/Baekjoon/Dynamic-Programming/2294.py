import sys
sys.stdin = open('input.txt')

n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dp = [10001] * (k+1)
dp[0] = 0

# i원을 만드는데 필요한 a원의 개수를 먼저 저장한다.
# 그 다음 a원의 가치로 i원을 만드는데 필요한 개수와 이전에 저장한 개수 중 최소 개수를 갱신한다.
# 핵심은 dp[i-a] / 5원 미만은 1원으로 만드는 경우의 수, 5원 이상은 1원과 5원으로 만드는 경우의 수, 12원 이상은 1원, 5원, 12원으로 만드는 경우의 수
for a in arr:
    for i in range(a, k+1):
        dp[i] = min(dp[i], dp[i-a]+1)   # dp[0]을 0으로 초기화했으므로, i원을 만들수록 동전이 1개씩 추가되므로 +1을 해줌

print(dp[k] if dp != 10001 else -1)