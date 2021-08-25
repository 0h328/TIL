import sys
sys.stdin = open('input.txt')

def dfs(row):
    global min_val, res
    if row == n:
        if min_val > res:
            min_val = res
    else:
        for i in range(n):
            if visited[i] == 0 and res + l[row][i] <= min_val:
                visited[i] = 1
                res += l[row][i]
                dfs(row+1)
                visited[i] = 0
                res -= l[row][i]



t = int(input())
for idx in range(1, t+1):
    n = int(input())
    s = {i for i in range(n)}
    l = [list(map(int, input().split())) for _ in range(n)]
    res = 0
    min_val = 10*n
    visited = [0]*n
    dfs(0)
    print('#{} {}'.format(idx, min_val))
