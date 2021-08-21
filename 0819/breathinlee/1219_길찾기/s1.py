import sys
sys.stdin = open("input.txt")

def dfs(v):
    visited[v] = 1
    for w in range(1, 100):
        if G[v][w] == 1 and not visited[w]:
            dfs(w)

for _ in range(10):
    tc, E = map(int, input().split())
    temp = list(map(int, input().split()))

    G = [[0] * 100 for _ in range(100)]
    visited = [0] * 100

    for i in range(E):
        G[temp[i * 2]][temp[i * 2 + 1]] = 1

    print('#{}'.format(tc), end=' ')

    dfs(0)
    if visited[99] == 1:
        print(1)
    else:
        print(0)
