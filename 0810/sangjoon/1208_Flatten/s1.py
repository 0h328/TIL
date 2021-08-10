import sys

sys.stdin = open("input.txt")

for test in range(1, 11):
    n = int(input())
    lst = list(map(int, input().split()))
    ans = 0

    while n > 0:
        max_h, min_h = max(lst), min(lst)

        if max_h - min_h == 0:
            break

        lst[lst.index(max_h)] -= 1
        lst[lst.index(min_h)] += 1
        n -= 1

    ans = max(lst) - min(lst)
    print("#{} {}".format(test, ans))
