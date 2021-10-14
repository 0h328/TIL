import sys

sys.stdin = open('input.txt')


def prim():
    for _ in range(V):
        min_idx = -1
        min_value = 11

        for i in range(V + 1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]
        visited[min_idx] = 1

        for i in range(V + 1):
            if not visited[i] and G[min_idx][i] < key[i]:
                key[i] = G[min_idx][i]

    return sum(key)

T = int(input())

for t in range(1, T + 1):
    V, E = map(int, input().split())  # V: 노드 수, E: 간선 수
    G = [[11 for _ in range(V+1)] for _ in range(V + 1)]
    key = [11] * (V + 1)
    key[0] = 0
    visited = [0] * (V + 1)

    for _ in range(E):
        start, end, W = map(int, input().split())
        G[start][end] = W
        G[end][start] = W

    print('#{} {}'.format(t, prim()))