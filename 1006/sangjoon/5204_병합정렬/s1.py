# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def divide(lst):
    if len(lst) == 1:
        return lst

    p = len(lst) // 2

    left = divide(lst[:p])
    right = divide(lst[p:])

    if left[-1] > right[-1]:
        res[1] += 1

    tmp = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            tmp.append(left[i])
            i += 1
        else:
            tmp.append(right[j])
            j += 1
    tmp += left[i:]
    tmp += right[j:]

    return tmp


ans = []
test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    res = [0, 0]
    res[0] = divide(lst)[n//2]
    ans.append("#{} {} {}".format(test, res[0], res[1]))

print(*ans, sep="\n")
