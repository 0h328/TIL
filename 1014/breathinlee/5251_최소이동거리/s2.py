import sys
sys.stdin = open('input.txt')

def dijkstra():
    for _ in range(N):
        min_idx = -1
        min_value = 1e9
        for i in range(N+1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = 1

        for j in range(N+1):
            if not visited[j] and dist[j] > dist[min_idx] + G[min_idx][j]:
                dist[j] = dist[min_idx] + G[min_idx][j]
    return dist[N]

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    G = [[1e9 for _ in range(N+1)] for _ in range(N+1)]
    dist = [1e9] * (N+1)
    dist[0] = 0
    visited = [0] * (N+1)
    for _ in range(E):
        s, e, w = map(int, input().split())
        G[s][e] = w

    result = dijkstra()
    print('#{} {}'.format(tc, result))