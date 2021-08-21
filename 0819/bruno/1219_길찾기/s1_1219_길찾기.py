def dfs(v):
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            for w in range(100):
                if G[v][w] == 1 and not visited[w]:
                    stack.append(w)


import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc, E = map(int, input().split())
    temp = list(map(int, input().split()))
    G = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(E):
        G[temp[i * 2]][temp[i * 2 + 1]] = 1

    visited = [0 for _ in range(100)]
    dfs(0)

    ans = 0
    if visited[99]:
        ans = 1
    print('#{} {}'.format(tc, ans))