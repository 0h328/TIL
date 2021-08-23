def dfs(start):
    stack = [start]

    while stack:
        start = stack.pop()

        if not visited[start]:
            visited[start] = 1

            for w in G[start]:
                stack.append(w)

    if visited[goal]:
        return 1

    return 0


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    G = [[] for _ in range(V+1)]
    for _ in range(E):
        s, e = list(map(int, input().split()))
        G[s].append(e)
    # print(G)

    visited = [0 for _ in range(V+1)]

    start, goal = map(int, input().split())
    # print(start, goal)

    print('#{} {}'.format(tc, dfs(start)))