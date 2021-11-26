# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def get_left(money, c):
    cnt = 0
    d, money = divmod(money, c)
    cnt += d

    return cnt, money


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    money = int(input())
    res = []
    cl = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    for c in cl:
        cnt, money = get_left(money, c)
        res.append(cnt)

    ans.append("#{}\n{}".format(test, " ".join(map(str, res))))

print(*ans, sep="\n")
