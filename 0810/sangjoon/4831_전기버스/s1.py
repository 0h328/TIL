import sys

sys.stdin = open("input.txt")


def dp(n):
    global available
    if n == 0:
        return -1

    lst = [dp(idx) for idx in range(n - k, n) if idx in stations]

    if lst:
        min_stations[n] = min(lst) + 1
        return min_stations[n]
    else:
        available = False
        return 0


test_case = int(input())
for test in range(1, test_case + 1):
    k, n, m = map(int, input().split())
    stations = list(map(int, input().split())) + [0]
    min_stations = [0] * (n + 1)
    available = True
    ans = dp(n)

    if not available:
        ans = 0

    print("#{} {}".format(test, ans))
