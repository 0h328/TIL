import sys
sys.stdin = open('input.txt')


def dfs(idx, pos):
    global ans

    if idx == N and pos > ans:
        ans = pos
        return

    if pos <= ans:
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(idx + 1, pos * arr[idx][i]/100)
            visited[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0

    dfs(0, 1)

    print('#{} {:.6f}'.format(t, ans*100))