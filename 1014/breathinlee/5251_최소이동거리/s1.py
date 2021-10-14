import sys
sys.stdin = open('input.txt')

# tc 4개 통과

def find(node, distance):
    global min_distance
    visited[node] = 1

    if node == N:
        if min_distance > distance:
            min_distance = distance
        return

    for t in range(1, N+1):
        if G[node][t] and not visited[t]:
            find(t, distance+G[node][t])
    visited[t] = 0


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    G = [[0] * (N + 1) for _ in range(N + 1)]
    visited = [0] * (N+1)
    min_distance = 1e9
    for _ in range(E):
        s, e, w = map(int, input().split())
        G[s][e] = w

    find(0, 0)
    print('#{} {}'.format(tc, min_distance))