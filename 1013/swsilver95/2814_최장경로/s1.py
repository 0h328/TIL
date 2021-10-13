import sys
sys.stdin = open('input.txt', 'r')

T = int(input())


def dfs(node, depth):
    global answer

    if answer < depth:
        answer = depth

    for p in graph[node]:
        if not visited[p]:
            visited[p] = 1
            dfs(p, depth + 1)
            visited[p] = 0


for tc in range(1, T + 1):
    N, M = map(int, input().split())

    if M != 0:
        graph = [[] for _ in range(N + 1)]

        for _ in range(M):
            parent, child = map(int, input().split())
            graph[parent].append(child)
            graph[child].append(parent)

        visited = [0] * (N + 1)
        answer = 0
        for node in range(1, N + 1):
            dfs(node, 0)
    else:
        answer = 1

    print('#{} {}'.format(tc, answer))