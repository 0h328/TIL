"""
1. 기본 정보
0번 지점에서 V번 지점까지 이동하는데 걸리는 최소 거리 출력
방향 존재

2. 입력 정보
첫 째 줄에 마지막 노드 번호 V(0번 부터 시작)와 간선의 개수 E
다음 줄부터 E개의 줄에 걸쳐 간선의 시작(start)과 끝(end) 그리고 구간의 거리(w) 정보

4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10

다익스트라
 - 시작 지점으로부터 특정 지점까지의 최소 거리(비용)을 아는 것이 포인트
  - 어떤 정점을 거쳐왔는지 알 수 없음
 - prim과 비슷한 방식으로 구현
  - 다만, 최소 비용을 갱신 하는 과정에서 차이가 발생
 - 음수 가중치 허용하지 않음
"""

def dijkstra():
    heap = []
    heapq.heappush(heap, (0, 0))                                # heap에 들어가는 순서 -> (가중치, 정점)

    while heap:                                                 # 힙이 비어있기 전까지
        w, v = heapq.heappop(heap)                              # 가중치, 정점 (최소힙 -> 최솟값 반환)
        if not visited[v]:                                      # 아직 방문하지 않았다면
            visited[v] = 1                                      # 방문처리
            dist[v] = w                                         # v 정점의 가중치 갱신
            for i in range(V+1):
                """
                  - 우선순위 큐를 활용한 경우 dist[i] > dist[v] + G[v][i] 조건 불필요
                  - min_heap은 항상 가장 작은 값이 루트에 존재 -> 방문하지 않은 경우만 처리하기 때문에 다른 값들이 들어있다고 해도 어차피 수행하지 않을 것
                """
                # if not visited[i] and dist[i] > dist[v] + G[v][i]
                if not visited[i]:
                     heapq.heappush(heap, (dist[v]+G[v][i], i))  # 가중치, 정점
    return dist[V]

import sys
import heapq
sys.stdin = open('input.txt')
V, E = map(int, input().split())                               # V: 마지막 노드 번호(0~V) / E: 간선
G = [[987654321 for _ in range(V+1)] for _ in range(V+1)]      # 가중치 초기화 (최소 거리를 구해야 하기 때문에 사용하지 않는 큰 값으로 초기화)
dist = [987654321] * (V+1)                                     # 비용(거리) 초기화
dist[0] = 0                                                    # 시작 정점 지점 (0번 -> 0번의 거리는 0)
visited = [0] * (V+1)                                          # 방문 체크
for _ in range(E):
    start, end, w = map(int, input().split())                  # 유향(방향있는) 그래프
    G[start][end] = w                                          # 시작 / 끝 / 가중치(길이)
print(dijkstra())                                              # 10