def dfs(v):
    stack = [v]
    while stack:
        v = stack.pop()
        if v == 99:
            return 1
        if not visited[v]:      # 방문 안했다면
            visited[v] = 1      # 방문체크
            for w in range(100):
                if G[v][w] == 1:     # 그 중 인접 정점
                    stack.append(w)
    return 0

import sys
sys.stdin = open('input.txt')

for _ in range(10):
    tc, E = map(int, input().split())
    temp = list(map(int, input().split()))
    G = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(E):
        G[temp[i * 2]][temp[i * 2 + 1]] = 1

    visited = [0 for _ in range(100)]
    # dfs(0)

    # ans = 0
    # if visited[99]:
    #     ans = 1
    print('#{} {}'.format(tc, dfs(0)))