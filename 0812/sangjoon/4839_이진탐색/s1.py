import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def binary_search(p: int, target: int):
    cnt = 0
    s, e = 1, p

    while s <= e:
        m = int((s + e) / 2)
        cnt += 1

        if m == target:
            return cnt

        if target > m:
            s = m
        else:
            e = m

    return p


test_case = int(input())

for test in range(1, test_case + 1):
    p, a, b = map(int, input().split())

    pa = binary_search(p, a)
    pb = binary_search(p, b)

    if pa == pb:
        ans = 0
    elif pa < pb:
        ans = "A"
    else:
        ans = "B"

    print("#{} {}".format(test, ans))