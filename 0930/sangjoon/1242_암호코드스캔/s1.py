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

    temp, res, chk = 0, 0, 0
    for _ in range(N):
        inp = list(map(lambda x: format(int(x, 16), "b"), input()))
        lst = []
        for c in inp:
            c = c.zfill(4)
            lst.extend(map(int, c))

        password_lst = []
        res_lst = []
        while lst:  # 암호가 있는 배열 탐색
            if lst[-1] == 1:
                for i in range(8):
                    pw = code.index(lst[-7:])
                    lst = lst[:-7]
                    if i % 2:
                        temp += pw*3
                        res += pw
                    else:
                        temp += pw
                        res += pw

                if not temp % 10:  # 검증코드가 옳은 경우
                    if res not in res_lst:
                        res_lst.append(res)
            else:
                lst.pop()

        ans = sum(res_lst)

    print("#{} {}".format(test, ans))
