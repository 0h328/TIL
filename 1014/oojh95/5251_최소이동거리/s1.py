import sys
sys.stdin = open('input.txt')


def dijkstra():
    for _ in range(N):
        min_idx = -1                                                        # 최소 인덱스 & 값 초기화
        min_value = 987654321
        for i in range(N+1):                                                # 최솟값 & 그때의 인덱스 찾기
            if not visited[i] and min_value > dist[i]:                      # 아직 i정점에 방문하지 않았고 dist[i]가 최솟값보다 작은 경우
                min_idx = i                                                 # 최솟값 인덱스 갱신
                min_value = dist[i]                                         # 최솟값 갱신
        visited[min_idx] = 1                                                # 최종 최솟값 갱신 후 방문처리

        for j in range(N+1):                                                # 인접 행렬에서 min_idx의 인접인 정점 중에서 최소 거리 갱신
            """
            A -> E        dist[j]
            A -> B -> E   dist[min_idx] + G[min_idx][j]
            """
            if not visited[j] and dist[j] > dist[min_idx] + G[min_idx][j]:  # 만약 j번 째를 방문하지 않았고
                                                                            # 바로 가려는 값(dist[j])이 거쳐가는 값(dist[min_idx] + G[min_idx][j])보다 더 크다면 == 더 짧은 거리로 이동 가능하다면
                dist[j] = dist[min_idx] + G[min_idx][j]                     # 그 값을 최소 거리로 갱신
    return dist[N]


T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    G = [[987654321 for _ in range(N + 1)] for _ in range(N + 1)]  # 가중치 초기화 (최소 거리를 구해야 하기 때문에 가중치로 사용하지 않는 큰 값으로 초기화)
    dist = [987654321] * (N + 1)  # 비용(거리) 초기화
    dist[0] = 0  # 시작 정점 지점 (0번 -> 0번의 거리는 0)
    visited = [0] * (N + 1)  # 방문 체크
    for _ in range(E):
        start, end, w = map(int, input().split())  # 유향(방향있는) 그래프
        G[start][end] = w  # 시작 / 끝 / 가중치(길이)
    print('#{} {}'.format(tc, dijkstra()))