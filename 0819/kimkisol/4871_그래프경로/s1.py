import sys

sys.stdin = open('input.txt')


def dfs(start, end):
    stack = [start]
    v = start
    while stack:
        for w in G[v]:
            if w == end:
                return 1
            if not visited[w]:
                visited[w] = 1
                stack.append(w)
                v = w
                break
        else: #모두 방문했거나 갈 수 있는 곳이 없을 경우 되돌아가기
            v = stack.pop()
    return 0


T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for i in range(E):
        start, end = map(int, input().split())
        G[start].append(end)

    start, end = map(int, input().split())

    print('#{} {}'.format(t, dfs(start, end)))
