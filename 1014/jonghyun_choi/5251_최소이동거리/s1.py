import sys
sys.stdin = open('input.txt')


def dijkstra():
    for i in range(N):
        min_idx = -1
        min_value = 987654321
        for j in range(N + 1):
            if not visited[j] and min_value > dist[i]:
                min_idx = j
                min_value = dist[j]

        visited[min_idx] = 1

        for j in range(N + 1):
            if not visited[j] and data[min_idx][j] != 987654321 and dist[j] > dist[min_idx] + data[min_idx][j]:
                dist[j] = dist[min_idx] + data[min_idx][j]
    return dist[N]



T = int(input())

for case in range(T):
    N, E = map(int, input().split())
    data = [[987654321] * (N + 1) for _ in range(N + 1)]
    dist = [987654321] * (N + 1)
    dist[0] = 0
    visited = [0] * (N + 1)
    for _ in range(E):
        d1, d2, distance = map(int, input().split())
        data[d1][d2] = distance
        data[d2][d1] = distance

    print('#{} {}'.format(case + 1, dijkstra()))