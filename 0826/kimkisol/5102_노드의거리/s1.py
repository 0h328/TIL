import sys

sys.stdin = open('input.txt')


def Distance(start, goal):
    global graph, visited
    Q = [start]
    visited[start] = 1
    while Q:
        v = Q.pop(0)
        for w in graph[v]:
            if w == goal:  # BFS는 도착했을 때가 거리가 최소가 됨
                return visited[v]
            if not visited[w]:
                visited[w] = visited[v] + 1
                Q.append(w)
    return 0  # 문제 조건을 잘 읽자!!!


T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for _ in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)  # 방향성이 없는 경우

    S, G = map(int, input().split())

    print('#{} {}'.format(t, Distance(S, G)))
