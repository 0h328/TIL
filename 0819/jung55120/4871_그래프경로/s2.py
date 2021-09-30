def dfs(start, goal):
    stack = [start]

    while stack:
        v = stack.pop()
        if not visited[v]:
            visited[v] = 1

            for w in G[v]:
                if visited[w]:
                    continue
                stack.append(w)


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())
        G[start].append(end)

    start, goal = map(int, input().split())

