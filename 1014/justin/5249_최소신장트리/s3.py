def prim():
    global ans
    while heap:
        w, v = heapq.heappop(heap)                      # w: 현재 가중치 / v: 현재 정점 -> 항상 최솟값이 반환
        if not visited[v]:                              # 정점을 아직 방문 안했다면
            ans += w                                    # v까지 이동한 가중치 누적
            visited[v] = 1                              # 해당 정점 선택하여 활용
            for w, weight in G[v]:                      # 인접 리스트에서 인접 정점(w)과 가중치(weight)를 가져와서
                if not visited[w]:                      # 그 정점(w)을 아직 체크 안했다면
                    heapq.heappush(heap, (weight, w))   # v와 연결되어 있는 모든 (가중치 + 인접 정점)을 추가
    return ans

import sys
import heapq
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())               # V개의 정점 -> 0부터 시작하기 때문에 개수는 +1이 된다는 점 유의
    G = [[] for _ in range(V+1)]                   # 인접 리스트
    ans = 0                                        # 누적 할 가중치
    visited = [0] * (V+1)                          # 정점의 선택 여부 체크
    heap = []
    heapq.heappush(heap, (0, 0))                   # item의 순서 -> (가중치, 정점)
    for i in range(E):
        start, end, W = map(int, input().split())  # 간선만큼 돌면서 두 정점과 가중치를 받고 인접 리스트 구현
        G[start].append((end, W))                  # 무방향 그래프 -> (정점, 가중치) 형태의 tuple로 append
        G[end].append((start, W))
    ans = prim()
    print('#{} {}'.format(tc, ans))