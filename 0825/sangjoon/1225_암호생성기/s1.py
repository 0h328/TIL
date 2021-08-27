# 문제 푼 시간
# 풀이법: Count 사용
import pathlib, sys
from collections import deque

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = 10

for test in range(1, test_case + 1):
    test = int(input())
    pw = list(map(int, input().split()))

    dq = deque(pw)
    hs = [i for i in range(1, 6)]
    idx = 1

    while dq:
        e = dq.popleft()
        tmp = e - hs[idx % 5]

        if tmp <= 0:
            dq.append(0)
            break

        dq.append(tmp)
        idx += 1

    ans = list(dq)
    print("#{}".format(test), end=" ")
    print(*ans)