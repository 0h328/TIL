import sys
sys.stdin = open('input.txt')

T = int(input())

def BFS(graph, start, end):
    q = []
    q.append(start)
    visited[start] = 1
    while q:
        next = q.pop(0)
        for i in range(len(graph[next])):
            if not visited[i] and graph[next][i] == 1:
                visited[i] = visited[next] + 1
                q.append(i)


        if visited[end]:
            return visited[end] - 1
    return 0



for case in range(T):
    V, E = map(int, input().split())
    Graph = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)
    for _ in range(E):
        A, B = map(int,input(). split())
        Graph[A][B] = 1
        Graph[B][A] = 1
    S, G = map(int,input().split())
    print('#{} {}'.format(case + 1,BFS(Graph,S,G)))
