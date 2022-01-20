import sys, time, datetime
start = time.time()
sys.stdin = open('input.txt')

N, M = map(int, input().split())
dp = [[0] * (M+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
# idx에 i-1, j-1이 있다면 idx를 맞춰주기 위해 [0,.., 0] 배열을 추가하는 것을 고민!

# (r+1, c) = dp[i-1][j]
# (r, c+1) = dp[i][j-1]
# (r+1 c+1) = dp[i-1][j-1]

# 실질적 배열은 (1, 1)부터 시작이므로 범위는 1 ~ N+1, M+1
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] += max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[-1][-1])

end = time.time()
sec = (end - start)
result = datetime.timedelta(seconds=sec)    # hh:mm:ss
print(result)


