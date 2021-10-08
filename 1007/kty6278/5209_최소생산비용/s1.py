import sys
sys.stdin = open('input.txt')

def dfs(row):
    global result, total
    if result < total:
        return

    if row == n:
        if total < result:
            result = total
            return

    for j in range(n):
        if not visited_col[j]:
            visited_col[j] = 1
            total += product[row][j]
            dfs(row + 1)
            total -= product[row][j]
            visited_col[j] = 0

for tc in range(int(input())):
    n = int(input())
    product = [list(map(int, input().split())) for _ in range(n)]
    visited_col = [0 for _ in range(n)]
    total = 0
    result = 99999999
    dfs(0)
    print('#{} {}'.format(tc+1, result))