import sys


def dfs(start, end):
    visited[start] = 1

    if start == end:
        return

    else:
        for idx in range(len(edges[start])):
            if not visited[edges[start][idx]]:
                dfs(edges[start][idx], end)


sys.stdin = open('input.txt')

T = int(input())
test_case = 1

while test_case <= T:
    V, E = map(int, input().split())
    edges = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        s, e = map(int, input().split())
        edges[s].append(e)

    S, G = map(int, input().split())
    # visited[S] = True
    dfs(S, G)

    ans = 0

    print('#{0} {1}'.format(test_case, visited[G]))
    # break
    test_case += 1
