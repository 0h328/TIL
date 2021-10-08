import sys
sys.stdin = open('input.txt')

def dfs(work, total):
    global tmp

    if total <= tmp:
        return

    if work == N:
        tmp = max(tmp, total)
        return

    for i in range(N):
        if not visited[i] and arr[work][i]:
            visited[i] = 1
            dfs(work + 1, total * arr[work][i] / 100)
            visited[i] = 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    tmp = 0
    dfs(0, 1)

    print('#{} {:.6f}'.format(tc, tmp * 100))


