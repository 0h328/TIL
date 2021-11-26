import sys

sys.stdin = open("input.txt")

T = int(input())


def dfs(n, k, total):
    global ans
    if total >= ans:
        return

    if n == k:
        if B <= total < ans:
            ans = total
        return

    dfs(n, k + 1, total)
    dfs(n, k + 1, total + data[k])


for tc in range(1, T + 1):
    N, B = map(int, input().split())
    data = list(map(int, input().split()))

    ans = 10000 * N
    dfs(N, 0, 0)
    print("#{} {}".format(tc, ans - B))
