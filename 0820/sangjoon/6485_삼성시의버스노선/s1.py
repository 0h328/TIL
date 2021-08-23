# 문제 푼 시간
# 풀이법: Count 사용
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())


def count_bus(c: int):
    cnt = 0
    for i in range(n):
        if route[i][0] <= c <= route[i][1]:
            cnt += 1

    return cnt


for test in range(1, test_case + 1):
    n = int(input())
    route = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    ans = []

    for i in range(p):
        c = int(input())
        ans.append(count_bus(c))

    print("#{} {}".format(test, " ".join(map(str, ans))))