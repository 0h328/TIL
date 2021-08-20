# 문제 푼 시간
# 풀이법: 구현
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(n)]
    check = [0] * 200  # 위 아래 통합

    for s, e in lst:  # 위치별 방문값
        ns, ne = (s - 1) // 2, (e - 1) // 2
        if ns < ne:
            for i in range(ns, ne + 1):
                check[i] += 1
        else:
            for i in range(ne, ns + 1):
                check[i] += 1

    ans = max(check)  # 방문 최대값
    print("#{} {}".format(test, ans))