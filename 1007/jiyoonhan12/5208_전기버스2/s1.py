import sys
sys.stdin = open('input.txt')

def dfs(idx, cnt):
    global ans

    if cnt >= ans:
        return

    if idx >= N:
        if cnt < ans:
            ans = cnt
        return

    for i in range(idx + M[idx], idx, -1):
        dfs(i, cnt+1)


T = int(input())
for t in range(1, T+1):
    M = list(map(int, input().split()))
    N = M[0]
    ans = 100

    dfs(1, 0)
    print('#{} {}'.format(t, ans-1))