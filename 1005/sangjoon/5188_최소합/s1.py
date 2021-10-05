# 문제 푼 시간
import pathlib
import sys


sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    mp = [list(map(int, input().split())) for _ in range(n)]

    for i in range(1, n):
        mp[0][i] += mp[0][i-1]
        mp[i][0] += mp[i-1][0]

    for i in range(1, n):
        for j in range(1, n):
            mp[i][j] = mp[i][j] + min(mp[i-1][j], mp[i][j-1])

    ans.append("#{} {}".format(test, mp[n-1][n-1]))
print(*ans, sep="\n")
