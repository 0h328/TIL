import sys
sys.stdin = open('input.txt')


def check(v):
    row = v[0]
    col = v[1]

    if adj[row][col]:
        return

    if row == 0:
        adj[row][col] = adj[row][col-1] + G[row][col]
        return

    if col == 0:
        adj[row][col] = adj[row-1][col] + G[row][col]
        return

    else:
        adj[row][col] = min(adj[row][col-1], adj[row-1][col]) + G[row][col]
        return


for tc in range(int(input())):
    N = int(input())
    G = [list(map(int, input().split())) for _ in range(N)]

    adj = [[0 for _ in range(N)] for _ in range(N)]

    adj[0][0] = G[0][0]

    for r in range(N):
        for c in range(N):
            check((r, c))

    print('#{0} {1}'.format(tc+1, adj[N-1][N-1]))
    # break
