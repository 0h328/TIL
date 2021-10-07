import sys
sys.stdin = open('input.txt')

def dfs(row, percent):
    global res
    if row == n:
        if res < percent:
            res = percent
        return
    elif res < percent:
        for i in range(n):
            if visited[i] == 0:
                visited[i] = 1
                dfs(row + 1, percent * p[row][i])
                visited[i] = 0

t = int(input())
for idx in range(1, t+1):
    n = int(input())
    p = [list(map(lambda x : float(x)/100, input().split())) for _ in range(n)]
    visited = [0] * n
    res = 0
    dfs(0, 1)
    print('#{} {:.6f}'.format(idx, round(res*100, 6)))