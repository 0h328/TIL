# 문제 푼 시간
# 풀이법: 수학
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    a, b = map(int, input().split())
    lst = list(map(int, input().split()))
    idx = b % a

    print("#{} {}".format(test, lst[idx]))