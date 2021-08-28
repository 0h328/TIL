# 문제 푼 시간
# 풀이법: Count 사용
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    a, b = input().split()
    cnt = a.count(b)

    ans = len(a) - len(b) * (cnt) + cnt

    print("#{} {}".format(test, ans))