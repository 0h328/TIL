import sys
sys.stdin = open('input.txt')

def dijkstra():
    for _ in range(V):
        min_idx = -1
        min_val = 9999999

        for i in range(V+1):
            if not v[i] and min_val > dist[i]:
                min_idx = i
                min_val = dist[i]
        v[min_idx] = 1

        for j in range(V+1):
            if not v[j] and dist[j] > dist[min_idx] + G[min_idx][j]:
                dist[j] = dist[min_idx] + G[min_idx][j]

    return dist[V]

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    G = [[9999999 for _ in range(V+1)] for _ in range(V+1)]
    dist = [9999999] * (V+1)
    dist[0] = 0
    v = [0] * (V+1)

    for _ in range(E):
        s, e, w = map(int, input().split())
        G[s][e] = w

    print('#{} {}'.format(tc, dijkstra()))

