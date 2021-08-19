import sys


def dfs(start, end):
    visited[start] = True

    if start == end:
        return

    else:
        for edge in edges:
            if edge[0] == start and not visited[edge[1]]:
                dfs(edge[1], end)


sys.stdin = open('input.txt')

T = int(input())
test_case = 1

while test_case <= T:
    V, E = map(int, input().split())
    edges = []
    visited = [False] * (V+1)

    for _ in range(E):
        edges.append(list(map(int, input().split())))

    S, G = map(int, input().split())
    # visited[S] = True
    dfs(S, G)

    ans = 0
    if visited[G] == 1:
        ans = 1
    print('#{0} {1}'.format(test_case, ans))
    # break
    test_case += 1
