import sys
sys.stdin = open('input.txt')


def dfs(i):
    global val, total
    if total < val:
        return

    if i == n:
        if total > val:
            val = total
            return

    for j in range(n):
        if not visited[j] and arr[i][j] != 0:
            visited[j] = 1
            total *= arr[i][j]
            dfs(i+1)
            total /= arr[i][j]
            visited[j] = 0


T = int(input())

for test_case in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    for r in range(n):
        for c in range(n):
            arr[r][c] /= 100
    visited = [0] * n
    val = 0
    total = 1
    dfs(0)
    ans = round(100 * val, 6)
    print('#{} {:.6f}'.format(test_case, ans))