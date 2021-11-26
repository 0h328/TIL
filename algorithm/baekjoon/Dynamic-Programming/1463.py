import sys
sys.stdin = open('input.txt')

N = int(input())
dp = [0] * (N+1)    # 각 인덱스가 1로 만들어질 때의 횟수를 채워줄 리스트

for i in range(2, N+1): # 1로 만드는 것이기 때문에, 0과 1은 의미가 없음
    # 오직, 1만 빼서 1을 만드는 횟수
    dp[i] = dp[i-1] + 1

    # i가 3과 2로 나누어질때, 1을 뺏을때와 비교해서 최소를 다시 갱신
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)

print(dp[N])



