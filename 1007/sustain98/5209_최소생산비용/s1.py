import sys
sys.stdin = open('input.txt')


def backtrack(index, acc):
    global res
    if index == n:
        if res > acc:
            res = acc
        return

    for i in range(n):
        if acc + l[index][i] < res and visited[i] == 0:
            visited[i] = 1
            backtrack(index + 1, acc + l[index][i])
            visited[i] = 0

t = int(input())
for idx in range(1, t+1):
    n = int(input())
    l = [list(map(int, input().split())) for _ in range(n)]
    res = 100*n
    visited = [0]*n

    backtrack(0, 0)

    print('#{} {}'.format(idx, res))