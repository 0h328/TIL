# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def check_num(n):
    chk = b[:] if n == 2 else t[:]
    for i in range(len(chk)):
        for j in range(n):
            tmp = chk[:]
            if j != tmp[i]:
                tmp[i] = str(j)
                num = int("".join(tmp), n)
                if num in check:
                    res[0] = num
                    return
                check[n-2].add(num)


ans = []
test_case = int(input())
for test in range(1, test_case + 1):
    b = list(input())
    t = list(input())
    check = [set(), set()]
    res = [0]
    # 3진수 변환
    check_num(2)
    check_num(3)
    res = check[0] & check[1]
    ans.append("#{} {}".format(test, list(map(int, res))[0]))

print(*ans, sep="\n")
