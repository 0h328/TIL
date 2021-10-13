import sys
sys.stdin = open('input.txt')

def dfs(s, cnt):
    global tmp

    if tmp < cnt:
        tmp = cnt

    if not v[s]:
        v[s] = 1

        for j in range(1, N+1):
            if adj[s][j] == 1 and not v[j]:
                dfs(j, cnt+1)
                v[j] = 0

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj = [[0 for _ in range(N+1)] for _ in range(N+1)]
    tmp = 0

    for _ in range(M):
        x, y = map(int, input().split())
        adj[x][y] = 1
        adj[y][x] = 1

    for i in range(1, N+1):
        v = [0] * (N+1)
        dfs(i, 1)

    print('#{} {}'.format(tc, tmp))