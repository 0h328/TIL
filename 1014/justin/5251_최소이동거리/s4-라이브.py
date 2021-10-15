import sys

sys.stdin = open('input_5251.txt', 'r')


def dijstra():
    dist = [987654321] * (V + 1)
    visited = [0] * (V + 1)

    dist[0] = 0

    for _ in range(V):
        min_idx = -1
        min_value = 987654321
        # 최소값 찾기
        for i in range(V + 1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = 1
        # 갱신할수 있으면 갱싄
        for i in range(V + 1):
            if not visited[i] and dist[i] > dist[min_idx] + adj_arr[min_idx][i]:
                dist[i] = dist[min_idx] + adj_arr[min_idx][i]

    return dist[V]


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V: 마지막 정점의번호, E 간선의 수

    adj_arr = [[987654321] * (V + 1) for _ in range(V + 1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        adj_arr[s][e] = w  # 유향 그래프 이니까

    print("#{} {}".format(tc, dijstra()))
