import pathlib, sys
from collections import deque


sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())
for test in range(1, test_case + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    sorted_lst = sorted(lst)
    dq = deque(sorted_lst)
    ans = []
    while dq:
        right = dq.pop()
        ans.append(right)

        if dq:
            left = dq.popleft()
            ans.append(left)

    print("#{}".format(test), end=" ")
    print(" ".join(map(str, lst[:10])))