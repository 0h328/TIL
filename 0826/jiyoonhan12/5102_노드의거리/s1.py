import sys
sys.stdin = open('input.txt')


def bfs(S):
    queue = []
    queue.append(S)
    visited[S] = 1

    while queue:
        t = queue.pop(0)
        for i in range(V + 1):
            if graph[t][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = visited[t] + 1


T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    graph = [[0] * (V+1) for _ in range(V+1)]

    for _ in range(E):
        v1, v2 = map(int, input().split())
        graph[v1][v2] = 1
        graph[v2][v1] = 1

    S, G = map(int, input().split())

    visited = [0] * (V+1)

    bfs(S)

    if visited[G]: # n번째 턴에 방문했다면 지나온 노드 수는 n-1
        res = visited[G]-1
    else:
        res = 0

    print('#{} {}'.format(t, res))