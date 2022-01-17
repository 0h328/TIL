import sys
sys.stdin = open('input.txt')

N = int(input())
arr = list(map(int, input().split()))

# 풀이1
# dp = arr[:]
#
# for i in range(1, N):
#     for j in range(i):
#         if arr[j] < arr[i]:
#             dp[i] = max(dp[i], arr[i]+dp[j])

# print(max(dp))

# 풀이2
dp = [0] * 1001

for a in arr:               # 배열 내 요소 순서대로
    dp[a] = a + max(dp[:a]) # 자신보다 낮은 숫자들이 누적된 합들과 자신을 더하면 됨

print(max(dp))