import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))
dp = [1001] * N     # 최소를 구해야 하므로 최댓값으로 지정
dp[0] = 0

for i in range(N):
    for j in range(1, arr[i]+1):            # dp list idx를 i+j로 해서 현재 idx + 점프 idx까지 값 갱신
        if i+j < N:                         # 미로 범위 안에서만 가능
            dp[i+j] = min(dp[i+j], dp[i]+1) # 현재 idx + 점프했을 때 idx로 계속 갱신

print(dp[N-1] if dp[N-1] != 1001 else -1)

