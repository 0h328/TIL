import sys
sys.stdin = open("input.txt")

def dfs(v):
    visited[v] = 1
    for w in range(1, V+1):
        if G[v][w] == 1 and visited[w] == 0:
            dfs(w)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    temp = [list(map(int, input().split())) for _ in range(E)]
    start, end = map(int, input().split())

    G = [[0] * (V+1) for _ in range(V+1)]
    for i in range(E):
        G[temp[i][0]][temp[i][1]] = 1

    visited = [0] * (V+1)

    dfs(start)
    print('#{}'.format(tc), end=' ')
    if visited[end] == 1:
        print(1)
    else:
        print(0)


