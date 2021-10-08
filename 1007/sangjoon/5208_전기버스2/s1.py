# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    lst = list(map(int, input().split()))
    n, m = lst[0], lst[1:]
    dp = [n]*n  # 최대값으로 초기화
    dp[0] = -1  # 시작점 초기화

    # dp로 최단경로 저장
    for i in range(n-1):
        for j in range(1, m[i]+1):
            if i+j < n:  # 이동기능 확인
                dp[i+j] = min(dp[i+j], dp[i]+1)
    dp[0] = 0

    ans.append("#{} {}".format(test, dp[-1]))

print(*ans, sep="\n")
