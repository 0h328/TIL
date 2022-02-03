import sys
sys.stdin = open('input.txt')

N, K = map(int, sys.stdin.readline().split())
dp = [0] * (K+1)

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    for j in range(K, W-1, -1):
        dp[j] = max(dp[j], dp[j-W] + V)

# 가방 무게의 최대 값 K 부터 역순으로 들어갈 물건의 무게 w까지 순회하면서
# 해당 위치의 최대 가치(cache[j])와 들어갈 물건의 무게 w 만큼
# 이전의 최대 가치(cache[j-w])에 물건의 가치 v를 더한 값 중 최대값을 구한다.
print(dp[-1])
