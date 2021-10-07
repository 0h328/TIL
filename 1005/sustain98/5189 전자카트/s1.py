import sys
sys.stdin = open('input.txt')


def dfs(x, s, acc):
    global res
    if len(s) == 0:
        if acc + l[x][0] < res:
            res = acc + l[x][0]
    elif res > acc:
        for i in s:
            dfs(i, s - {i}, acc + l[x][i])


t = int(input())
for idx in range(1, t+1):
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    res = 1e19
    dfs(0, {i for i in range(1, n)}, 0)

    print('#{} {}'.format(idx, res))