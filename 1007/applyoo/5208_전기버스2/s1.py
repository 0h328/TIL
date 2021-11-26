import sys
sys.stdin = open('input.txt')


def dfs(cur, cnt):
    global res
    if cnt >= res:
        return

    if cur >= len(A):
        res = cnt
        return

    for i in range(A[cur], 0, -1):
        dfs(cur+i, cnt+1)


ans = []
T = int(input())
for tc in range(1, T + 1):
    N, *A = map(int, input().split())

    res = 100
    dfs(0, 0)
    ans.append('#{0} {1}'.format(tc, res-1))

print(*ans, sep='\n')
