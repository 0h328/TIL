# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    N, M = map(int, input().split())
    code = [
        [0, 0, 0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0, 0, 1],
        [0, 0, 1, 0, 0, 1, 1],
        [0, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 1, 1],
        [0, 1, 1, 0, 0, 0, 1],
        [0, 1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 0, 1, 1],
    ]

    temp, ans, chk = 0, 0, 0
    for _ in range(N):
        lst = list(map(int, list(input())))

        if chk:  # 이미 검증이 끝난경우
            continue

        while lst:  # 암호가 있는 배열 탐색
            if lst[-1] == 1:
                break
            else:
                lst.pop()

        if lst:  # 암호 검증 시작
            chk = 1
            temp += code.index(lst[-7:])
            ans += code.index(lst[-7:])
            for i in range(1, 8):
                pw = code.index(lst[(i+1)*(-7):(i)*(-7)])
                if i % 2:
                    temp += pw*3
                    ans += pw
                else:
                    temp += pw
                    ans += pw

            if temp % 10:  # 검증코드가 틀린 경우
                ans = 0

    print("#{} {}".format(test, ans))
