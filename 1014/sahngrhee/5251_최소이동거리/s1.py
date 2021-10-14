import sys
sys.stdin = open('input.txt')


def dijkstra():
    for _ in range(V):
        min_idx = -1
        min_value = 987654321
        for i in range(V+1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = 1

        for j in range(V+1):
            if not visited[j] and dist[j] > dist[min_idx] + G[min_idx][j]:
                dist[j] = dist[min_idx] + G[min_idx][j]
    return dist[V]


T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    G = [[987654321 for _ in range(V+1)] for _ in range(V+1)]
    dist = [987654321] * (V+1)
    dist[0] = 0
    visited = [0] * (V+1)
    for _ in range(E):
        start, end, w = map(int, input().split())
        G[start][end] = w
    dijkstra()
    print('#{} {}'.format(test_case, dist[V]))