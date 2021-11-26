# 문제 푼 시간
# 풀이법: 큐 사용
import pathlib, sys
from collections import deque

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def pizza_pit():
    dq = deque(pizza[:n])
    left = pizza[n:]
    cnt = m

    while cnt > 1:
        idx, cheeze = dq.popleft()

        if cheeze // 2:  # 치즈가 남았을 경우
            dq.append([idx, cheeze // 2])
        else:  # 치즈가 남지 않았을 경우
            cnt -= 1
            if left:  # 남은 피자가 있을 경우
                dq.append(left.pop(0))

    return dq[0][0]  # 하나 남은 피자의 idx


test_case = int(input())

for test in range(1, test_case + 1):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))

    pizza = []
    for idx, p in enumerate(lst, start=1):
        pizza.append([idx, p])

    ans = pizza_pit()

    print("#{} {}".format(test, ans))