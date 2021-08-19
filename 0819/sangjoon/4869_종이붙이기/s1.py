# 문제 푼 시간
# 풀이법: 메모이제이션 DP 사용
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def dp(n: int):
    n //= 10

    for i in range(2, n):
        case.append(case[i - 2] * 2 + case[i - 1])

    return case[-1]


test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    case = [1, 3]
    ans = get_tape_case(n)

    print("#{} {}".format(test, ans))