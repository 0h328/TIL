import sys
sys.stdin = open('input.txt')

def dfs(row, total):
    global result
    if result >= total:
        return

    if row == n:
        if total > result:
            result = total
            return

    for j in range(n):
        if not visited_col[j]:
            visited_col[j] = 1
            dfs(row + 1, total * product[row][j]/100)
            visited_col[j] = 0

for tc in range(int(input())):
    n = int(input())
    product = [list(map(int, input().split())) for _ in range(n)]
    visited_col = [0 for _ in range(n)]
    result = 0
    dfs(0, 1)
    result = '{:.6f}'.format(round(result*100, 6))
    print('#{} {}'.format(tc+1, result))