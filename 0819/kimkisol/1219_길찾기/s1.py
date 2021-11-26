import sys

sys.stdin = open('input.txt')


def dfs(start=0, end=99):
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
        else:  # 모두 방문했거나 갈 수 있는 곳이 없을 경우 되돌아가기
            v = stack.pop()
    return 0


for t in range(1, 11):
    tc, E = map(int, input().split())
    routes = list(map(int, input().split()))
    G = [[] for _ in range(100)]
    visited = [0] * (100)

    for i in range(0, E * 2, 2):
        G[routes[i]].append(routes[i + 1])

    print('#{} {}'.format(t, dfs()))
