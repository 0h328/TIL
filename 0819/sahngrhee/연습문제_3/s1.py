def dfs(v):
    stack = [v]
    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1
            print('방문 정점: {}, 방문 체크: {}'.format(v, visited))
            for w in range(1, V+1):
                if G[v][w] == 1 and not visited[w]:
                    stack.append(w)

import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
temp = list(map(int, input().split()))
G = [[0 for _ in range(V+1)] for _ in range(V+1)]
visited = [0 for _ in range(V+1)]
for i in range(E):
    G[temp[i*2]][temp[i*2+1]] = 1
    G[temp[i*2+1]][temp[i*2]] = 1
dfs(1)