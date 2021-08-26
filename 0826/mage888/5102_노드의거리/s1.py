import sys
sys.stdin = open('input.txt')

def bfs(S, G):
    q = []
    q.append(S)
    visited[S] = 0
    while q:
        t = q.pop(0)
        for i in graph[t]:
            if not visited[i]:
                q.append(i)
                visited[i] = visited[t] + 1

    return visited[G]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    # print(graph)

    for _ in range(E):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    # print(graph)

    S, G = map(int, input().split())

    visited = [0] * (V+1)

    print('#{} {}'.format(tc, bfs(S, G)))