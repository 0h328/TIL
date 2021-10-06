import sys
sys.stdin = open('input.txt')


def dfs(idx, c):
    global res
    if c >= res:
        return
    if len(v) == N:
        if res > c + arr[idx][0]:
            res = c + arr[idx][0]
        return

    for i in range(N):
        if i not in v:
            v.add(i)
            dfs(i, c+arr[idx][i])
            v.remove(i)


ans = []
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    res = 1200
    v = set([0])

    dfs(0, 0)
    ans.append('#{0} {1}'.format(tc, res))

print(*ans, sep='\n')
