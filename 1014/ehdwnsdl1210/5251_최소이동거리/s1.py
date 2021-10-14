import sys
sys.stdin = open('input.txt')

def dijkstra():
    for _ in range(N):
        min_idx = -1
        min_value = 987654321
        for i in range(N+1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = 1

        for j in range(N+1):
            """
            A -> E        dist[j]
            A -> B -> E   dist[min_idx] + grp[min_idx][j]
            """
            if not visited[j] and dist[j] > dist[min_idx] + grp[min_idx][j]:

                dist[j] = dist[min_idx] + grp[min_idx][j]
    return dist[N]

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    grp = [[987654321] * (N+1) for _ in range(N+1)]
    dist = [987654321] * (N+1)
    dist[0] = 0
    visited = [0] * (N+1)
    for i in range(E):
        s, e, w = map(int, input().split())
        grp[s][e] = w
    # print(grp)

    print('#{} {}'.format(tc, dijkstra()))
#1 2
#2 4
#3 10