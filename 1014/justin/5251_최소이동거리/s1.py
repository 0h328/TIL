"""
- 다익스트라에서는 왜 가중치(비용)이 작은 정점부터 탐색
 -> 완전 탐색을 하지 않으려고 하기 때문
- 음의 가중치를 못 쓰는 이유는?
 -> 다른 경로를 택했을 때 비용이 작아진다.
"""
def dijkstra():
    for _ in range(V):
        min_idx = -1
        min_value = 987654321
        for i in range(V+1):                           # 최솟값과 그때의 인덱스 찾기
            if not visited[i] and min_value > dist[i]: # 아직 i정점에 방문하지 않았고 dist[i]가 최솟값보다 작은 경우
                min_idx = i                            # 최솟값 인덱스 갱신
                min_value = dist[i]                    # 최솟값 갱신
        visited[min_idx] = 1                           # 최종 최솟값 갱신 후 방문처리
        for j in range(V+1):                           # 최소 거리 갱신
            """
            A -> E        dist[j]
            A -> B -> E   dist[min_idx] + G[min_idx][j]
            """
            if not visited[j] and dist[j] > dist[min_idx] + G[min_idx][j]:  # 만약 j번 째를 방문하지 않았고
                                                                            # 바로 가려는 값(dist[j])이 거쳐가는 값(dist[min_idx] + G[min_idx][j])보다 더 크다면 ==> 더 짧은 거리로 이동 가능하다면
                dist[j] = dist[min_idx] + G[min_idx][j]                     # 그 값을 최소 거리로 갱신
    return dist[V]                                                          # 마지막 V번 지점까지의 거리

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())                                        # V: 마지막 노드 번호(0 ~ V) / E: 간선
    G = [[987654321 for _ in range(V + 1)] for _ in range(V + 1)]           # 가중치 초기화 (최소 거리를 구해야 하기 때문에 가중치로 사용하지 않는 큰 값으로 초기화)
    dist = [987654321] * (V+1)                                              # 비용(거리) 초기화
    dist[0] = 0                                                             # 시작 지점 (0번 -> 0번의 거리는 0)
    visited = [0] * (V+1)                                                   # 방문 체크
    for _ in range(E):
        start, end, w = map(int, input().split())                           # 유향 그래프
        G[start][end] = w
    ans = dijkstra()
    print('#{} {}'.format(tc, ans))